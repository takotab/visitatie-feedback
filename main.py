import argparse
import os
import logging


parser = argparse.ArgumentParser(description="Handeling the results of the visitatie.")

parser.add_argument(
    "--map",
    default="data_fake",
    type=str,
    help="Select the map to be used for making the results.",
)
args = parser.parse_args()


def main(map):
    
    # TODO extract patient x as dict
    # TODO 2 meetinstumenten
    # TODO STartBack/GPE
    # TODO Dossiertoets
    # TODO Check num of patienten vs expected
    # TODO Save praktijk_dict as json
    # TODO make pdf rapport
    pass


if __name__ == "__main__":
    main(args.map)
