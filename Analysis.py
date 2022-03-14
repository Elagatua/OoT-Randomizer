#!/usr/bin/env python3
import argparse
import logging
import textwrap
import statistics
import sys

from Main import main
from Utils import check_python_version
from Settings import get_settings_from_command_line_args


class ArgumentDefaultsHelpFormatter(argparse.RawTextHelpFormatter):

    def _get_help_string(self, action):
        return textwrap.dedent(action.help)


def start():

    settings, gui, args_loglevel, no_log_file = get_settings_from_command_line_args()

    # set up logger
    loglevel = {'error': logging.ERROR, 'info': logging.INFO, 'warning': logging.WARNING, 'debug': logging.DEBUG}[args_loglevel]
    logging.basicConfig(format='%(message)s', level=loglevel)

    logger = logging.getLogger('')

    try:
        all_counts = []
        all_longest_paths = []

        for i in range(200):
          settings.update_seed('')
          spoiler = main(settings)
          path_power = spoiler.goal_locations[0]['triforce_hunt']['power'][0]
          path_wisdom = spoiler.goal_locations[0]['triforce_hunt']['wisdom'][0]
          path_courage = spoiler.goal_locations[0]['triforce_hunt']['courage'][0]
          counts = [
            len(path_power),
            len(path_wisdom),
            len(path_courage)
          ]
          longest_path = max(counts)
          all_counts.extend(counts)
          all_longest_paths.append(longest_path)
        
        print(all_counts)
        print(all_longest_paths)

        for i in range(2):
          data_source = all_counts if i == 0 else all_longest_paths
          prefix = '' if i == 0 else 'longest '

          print()
          print(prefix + 'path median:', statistics.median_high(data_source))
          print(prefix + 'path avg:', round(statistics.mean(data_source), 2))
          print(prefix + 'path stdev:', round(statistics.stdev(data_source), 2))
          if i == 0:
            print(prefix + 'path max:', max(data_source))
          
          print([round(q, 1) for q in statistics.quantiles(data_source, n=10)])
        
    except Exception as ex:
        logger.exception(ex)
        sys.exit(1)


if __name__ == '__main__':
    check_python_version()
    start()
