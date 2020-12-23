# -*- coding:utf-8 -*-
# @author: Marssssssss


DEP_LIST = []


class MultiExpFilter(object):
	""" This filter use for expression by |.
		e.g.: 
			<a> = <b> | <c>
			->
			<a> = <b>
			<a> = <c>
	"""
	def __init__(self):
		self._lines = []
		self._splited_equation = {}  # {left: [exp1, exp2...]}

	def do_filter(self, content):
		""" 
		Filter out all expression from content.
		:param content: content to filter.
		:return: all single expression.
		"""
		lines = self._content_spliter(content)
		jointed_lines = self._line_joint(lines)
		paired_lines = self._line_pairer(jointed_lines)
		all_pairs = self._line_sperater(paired_lines)
		return all_pairs

	def _content_spliter(self, content):
		"""
		Split content to line.
		:param content: content to splited.
		:return: line list.
		"""
		lines = content.split("\n")
		return lines

	def _line_joint(self, lines):
		"""
		Joint lines by /.
		:param lines: lines to joint.
		:return: lines jointed.
		"""
		ret = []
		jointed_line = ""
		for line in lines:
			if not line.endswith("\\"):
				ret.append(jointed_line + line)
				jointed_line = ""
				continue
			jointed_line += line[:-1]
		return ret

	def _line_pairer(self, lines):
		"""
		Seperate line by = and store them to a tuple.
		:param lines: lines to pair.
		:return: lines paired.
		"""
		ret = []
		for line in lines:
			idx = line.find("=")
			if idx != -1:
				ret.append((line[:idx].strip(), line[idx + 1:]))
			else:
				raise Exception("[Error]An expression should has =: %s" % line)
		return ret

	def _line_sperater(self, pairs):
		"""
		Seperate pair by |.
		:param pair: pair to seperate.
		:return: sperated pairs.
		"""
		ret = {}
		for pair in pairs:
			head = pair[0]
			exp = pair[1]
			dealt_line = ""
			dep_switch = True
			exp_list = []
			# deal with line
			for c in exp:
				if dep_switch:
					if c == "\\":
						dep_switch = False
						continue
					elif c == "|":
						exp_list.append(dealt_line)
						dealt_line = ""
						continue
					elif c.strip() == "" or c in DEP_LIST:
						continue
				else:
					dep_switch = True
				dealt_line += c
			if dealt_line != "":
				exp_list.append(dealt_line)
			ret[head] = exp_list
		return ret
	

if __name__ == "__main__":
	mef = MultiExpFilter()
	print(mef.do_filter("<as> = <de> |  <\<fc>\\\n\\\"<as> \n <as2123>=  <as> + <ass> | <test>"))	
