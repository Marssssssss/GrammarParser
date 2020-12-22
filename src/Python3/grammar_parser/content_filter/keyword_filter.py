# -*- coding:utf-8 -*-
# @author: Marssssssss


STATE_MAP = {
	# -1 mean every state, "" means every char
	("<", 0): (True, 1),
	("<", 1): (False, "Error!!Check about <."),
	(">", 0): (False, "Error!!Maybe you need \\?"),
	(">", 1): (True, 0),
	("\\", 0): (True, 2),
	("\\", 1): (True, 3),
	("", 1): (True, 1),
	("", 2): (True, 0),
	("", 3): (True, 1),
	("", 0): (True, 0),
}
IDENT_SIGN = "<>\\"
CAN_QUIT_STATE = [0]
CAN_STORE_STATE = [1, 3]


def _map_next(char, state):
	if (char, state) in STATE_MAP:
		return STATE_MAP[(char, state)]
	if ("", state) in STATE_MAP:
		return STATE_MAP[("", state)]
	state = -1
	return STATE_MAP.get((char, state), None)


class KeywordFilter(object):
	"""Keywrod grammar(surround with < and >): <keyword>
	"""
	def __init__(self):
		self._word = ""
		self._ret = set()

	def do_filter(self, content):
		""" 
		Seperate all word surrounded by < and > from content to a set.
		Return the dict.
		:param content: content to filter.
		:return: set 
		"""
		self._word = ""
		self._ret = set()
		st = 0
		word = ""
		for c in content:
			state = self._char_process(c, st)
			self._state_jump_process(st, state, c)
			st = state
		ret = set()
		ret.update(self._ret)
		return ret

	def _char_process(self, nextc, state):
		"""
		Get next char and current state, return new state.
		:param next: next char.
		:return: a state
		"""
		next_tup = _map_next(nextc, state)
		if next_tup is None:
			import traceback
			traceback.print_stack()
			raise Exception("Error occurred when filter keyword.")
		succ = next_tup[0]
		if succ:
			return next_tup[1]
		else:
			raise Exception(next_tup[1])

	def _state_jump_process(self, old, new, c):
		"""
		Get the jump behav func and call it. Func name: _on_state_jump_'old'_'new'
		:param old: old state
		:param new: new state
		"""
		func = getattr(self, "_on_state_jump_" + str(old) + "_" + str(new), None)
		if func is not None and callable(func):
			func(old, new, c)

	def _on_state_jump_1_0(self, old, new, c):
		""" from state 1 to state 0
		"""
		self._ret.update({self._word + c})
		self._word = ""

	def _on_state_jump_1_1(self, old, new, c):
		""" from state 0 to state 0
		"""
		self._word += c

	_on_state_jump_0_1 = _on_state_jump_1_1
