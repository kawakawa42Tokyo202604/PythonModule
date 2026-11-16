"""Behavior checks across the eleven independent Python modules."""

import importlib.util
import os
from pathlib import Path
import subprocess
import sys
from types import ModuleType
from typing import Any

import pytest
from pydantic import ValidationError

ROOT = Path(__file__).resolve().parents[1]


def load(relative: str) -> ModuleType:
    """Load an exercise without mixing independently named modules."""
    name = relative.replace("/", "_").replace(".", "_")
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def execute(relative: str, cwd: Path, *args: str,
            stdin: str = "") -> subprocess.CompletedProcess[str]:
    """Run an independent CLI in a disposable working directory."""
    env = os.environ.copy()
    env["MPLBACKEND"] = "Agg"
    return subprocess.run(
        [sys.executable, str(ROOT / relative), *args], cwd=cwd,
        input=stdin, capture_output=True, text=True, timeout=30, env=env,
    )


def test_module00_input_and_arithmetic(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str],
) -> None:
    module = load("python_module00/ex2/ft_plot_area.py")
    answers = iter(["5", "7"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    module.ft_plot_area()
    assert "Plot area: 35" in capsys.readouterr().out


def test_module01_growth_tracks_state() -> None:
    module = load("python_module01/ex6/ft_garden_analytics.py")
    plant = module.Plant("Rose", 10.0, 3)
    plant.grow(2.5)
    plant.age(4)
    assert plant.height == 12.5 and plant.age_val == 7
    assert module.Plant.create_anonymous().name == "Unknown plant"


def test_module02_cleanup_runs_after_error(tmp_path: Path) -> None:
    result = execute("python_module02/ex4/ft_finally_block.py", tmp_path)
    assert result.returncode == 0, result.stderr
    assert "Caught PlantError" in result.stdout
    assert result.stdout.count("Closing watering system") == 2


def test_module03_score_cli_handles_valid_and_invalid_values(
    tmp_path: Path,
) -> None:
    script = "python_module03/ex1/ft_score_analytics.py"
    result = execute(script, tmp_path, "10", "20", "bad", "30")
    assert result.returncode == 0, result.stderr
    assert "Total score: 60" in result.stdout
    assert "Average score: 20.0" in result.stdout
    assert "Invalid parameter: 'bad'" in result.stdout
    assert "No scores provided" in execute(script, tmp_path).stdout


def test_module04_file_transformation_and_missing_file(
    tmp_path: Path,
) -> None:
    source = tmp_path / "source.txt"
    output = tmp_path / "result.txt"
    source.write_text("alpha\nbeta\n", encoding="utf-8")
    script = "python_module04/ex1/ft_archive_creation.py"
    result = execute(script, tmp_path, str(source), stdin=str(output) + "\n")
    assert result.returncode == 0, result.stderr
    assert output.read_text(encoding="utf-8") == "alpha#\nbeta#\n"
    missing = execute(script, tmp_path, str(tmp_path / "absent.txt"))
    assert missing.returncode != 0 and "Error opening file" in missing.stdout


def test_module05_processors_reject_invalid_input_and_keep_order() -> None:
    module = load("python_module05/ex0/data_processor.py")
    processor = module.NumericProcessor()
    processor.ingest([1, 2.5])
    assert processor.output() == (0, "1")
    assert processor.output() == (1, "2.5")
    with pytest.raises(IndexError):
        processor.output()
    with pytest.raises(ValueError):
        processor.ingest(True)


def test_module06_package_imports(tmp_path: Path) -> None:
    result = subprocess.run(
        [sys.executable, "-c", "from alchemy.elements import create_earth; "
         "from alchemy.grimoire import light_spellbook; "
         "assert create_earth() == 'Earth element created'"],
        cwd=ROOT / "python_module06", capture_output=True, text=True,
        timeout=15,
    )
    assert result.returncode == 0, result.stderr


def test_module07_capability_composition(tmp_path: Path) -> None:
    result = execute("python_module07/capacitor.py", tmp_path)
    assert result.returncode == 0, result.stderr
    assert "healing capability" in result.stdout
    assert "transform capability" in result.stdout


def test_module08_environment_and_real_plot(tmp_path: Path) -> None:
    result = execute("python_module08/ex0/construct.py", tmp_path)
    assert result.returncode == 0, result.stderr
    assert "isolated environment" in result.stdout
    result = execute("python_module08/ex1/loading.py", tmp_path)
    assert result.returncode == 0, result.stderr
    assert "[MISSING]" not in result.stdout
    images = list(tmp_path.glob("*.png"))
    assert images and all(p.stat().st_size > 0 for p in images)


def test_module09_valid_and_invalid_crew_data() -> None:
    module = load("python_module09/ex0/space_station.py")
    fields: dict[str, Any] = {
        "station_id": "ISS001", "name": "Station", "crew_size": 3,
        "power_level": 90, "oxygen_level": 95,
        "last_maintenance": "2026-01-01T00:00:00",
    }
    assert module.SpaceStation(**fields).crew_size == 3
    for size in (0, 21):
        with pytest.raises(ValidationError):
            module.SpaceStation(**dict(fields, crew_size=size))


def test_module10_higher_order_functions() -> None:
    module = load("python_module10/ex1/higher_magic.py")

    def spell(target: str, power: int) -> str:
        return f"{target}:{power}"

    assert module.power_amplifier(spell, 3)("Dragon", 4) == "Dragon:12"
    assert module.spell_sequence([spell, spell])("A", 2) == ["A:2", "A:2"]
    caster = module.conditional_caster(lambda _, power: power > 2, spell)
    assert caster("A", 1) == "Spell fizzled"
    assert caster("A", 3) == "A:3"
