import operator
import re

OPERATORS = {
	"+": operator.add,
	"*": operator.mul
}

def evaluate_simple_expression_linearly(expression):
	components = expression.split()
	result = 0
	next_operator = operator.add
	for component in components:
		if component.isnumeric():
			number = int(component)
			result = next_operator(result, number)
		else:
			next_operator = OPERATORS[component]
	return result

def evaluate_simple_expression_part_2(expression):
	additions = re.findall("(?:(?:[0-9]+)* \+ [0-9]+)+", expression)
	for addition in additions:
		numbers = [int(num) for num in addition.split(" + ")]
		expression = expression.replace(addition, str(sum(numbers)), 1)
	return evaluate_simple_expression_linearly(expression)

def evaluate_expression(expression, simple_expression_evaluator):
	inner_brackets = re.findall("\([^()]+\)", expression)
	while len(inner_brackets) > 0:
		for exp in inner_brackets:
			simple_exp = re.sub("[()]", "", exp)
			expression = expression.replace(
				exp,
				str(evaluate_expression(simple_exp, simple_expression_evaluator)),
				1)
		
		inner_brackets = re.findall("\([^()]+\)", expression)
	
	return simple_expression_evaluator(expression)

with open("18.txt") as file:
	expressions = file.read().split("\n")

results = []
for expression in expressions:
	result = evaluate_expression(expression, evaluate_simple_expression_linearly)
	results.append(result)
print(sum(results))

results = []
for expression in expressions:
	result = evaluate_expression(expression, evaluate_simple_expression_part_2)
	results.append(result)
print(sum(results))