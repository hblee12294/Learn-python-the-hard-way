from nose.tools import *
from ex49 import parser

def test_sentence():
	sentence = parser.Sentence(('noun', 'bear'), ('verb', 'eat'), ('noun', 'girl'))
	assert_equal(sentence.subject, 'bear')
	assert_equal(sentence.verb, 'eat')
	assert_equal(sentence.object, 'girl')
	
	
def test_peek():
	assert_equal(parser.peek([('noun', 'princess')]), 'noun')

	
def test_match():
	assert_equal(parser.match([('noun', 'princess')], 'noun'), ('noun', 'princess'))
	
	
def test_skip():
	words = [('stop', 'the'), ('noun', 'girl')]
	parser.skip(words, 'stop')
	assert_equal(words, [('noun', 'girl')])


def test_parse_verb():
	assert_raises(parser.ParserError, parser.parse_verb, [('noun', 'bear')])

	
def test_parse_object():
	assert_raises(parser.ParserError, parser.parse_object, [('verb', 'go')])
	

def test_parse_subject():
	sentence = parser.parse_subject([('verb', 'eat'), ('noun', 'princess')], ('noun', 'bear'))
	assert_equal(sentence.subject, 'bear')
	assert_equal(sentence.verb, 'eat')
	assert_equal(sentence.object, 'princess')

	
def test_parse_sentence():
	assert_raises(parser.ParserError, parser.parse_sentence, [('adjective', 'pretty')])					