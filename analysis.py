from radon.visitors import ComplexityVisitor
from radon.cli import Config
from radon.complexity import cc_rank, SCORE
from radon.cli import Config
from radon.cli.harvest import CCHarvester
from radon.complexity import cc_rank, cc_visit, average_complexity
from radon.metrics import mi_visit, mi_rank
from pylint.lint import Run
from pylint import lint
from pylint.reporters.text import TextReporter
import json


class WritableObject(object):
    def __init__(self):
        self.content = []
    def write(self, st):
        self.content.append(st)
    def read(self):
        return self.content

def cyclomaticComplexity(code):
    for member in cc_visit(code):
        blockType = member.letter
        blockComplexity = member.complexity
        blockRank = cc_rank(blockComplexity)
        blockFullName = member.fullname
    return [average_complexity(cc_visit(code)), cc_rank(average_complexity(cc_visit(code)))]


def maintainabilityIndex(code):
    miScore = mi_visit(code, True)
    miRank = mi_rank(miScore)
    return [miScore, miRank]

def run_pylint(filename):
    ARGS = []  # put your own here
    pylint_output = WritableObject()
    lint.Run([filename]+ARGS, reporter=TextReporter(pylint_output), exit=False)
    fullText = ""
    for l in pylint_output.read():
        fullText = fullText + l + "\n"
    return fullText
