"""Run the function-only exercises from Python Module 00."""

import argparse
from collections.abc import Callable

from ex0.ft_hello_garden import ft_hello_garden
from ex1.ft_garden_name import ft_garden_name
from ex2.ft_plot_area import ft_plot_area
from ex3.ft_harvest_total import ft_harvest_total
from ex4.ft_plant_age import ft_plant_age
from ex5.ft_water_reminder import ft_water_reminder
from ex6.ft_count_harvest_iterative import ft_count_harvest_iterative
from ex6.ft_count_harvest_recursive import ft_count_harvest_recursive
from ex7.ft_seed_inventory import ft_seed_inventory


def main() -> None:
    exercises: dict[str, Callable[[], None]] = {
        "0": ft_hello_garden,
        "1": ft_garden_name,
        "2": ft_plot_area,
        "3": ft_harvest_total,
        "4": ft_plant_age,
        "5": ft_water_reminder,
        "6": ft_count_harvest_iterative,
        "6-recursive": ft_count_harvest_recursive,
    }
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "exercise", nargs="?", default="0", choices=[*exercises, "7"]
    )
    parser.add_argument("--seed-type", default="carrot")
    parser.add_argument("--quantity", type=int, default=10)
    parser.add_argument("--unit", choices=["packets", "grams", "area"],
                        default="packets")
    args = parser.parse_args()
    if args.exercise == "7":
        ft_seed_inventory(args.seed_type, args.quantity, args.unit)
    else:
        exercises[args.exercise]()


if __name__ == "__main__":
    main()
