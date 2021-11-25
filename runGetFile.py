from data.paths import pathToDataDirWithOs, test
from production.defaultSetupLogger import defaultSetupLogger
log = defaultSetupLogger(__file__)
import os


def main():
    log.debug(test)

main()

    