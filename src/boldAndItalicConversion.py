import re


def convertBold(textVal):
  markdownPattern = r'(\*\*)([^\*]*)(\*\*)'
  returnText = re.sub(markdownPattern, processBoldMatch, textVal)
  return returnText

def convertItalic(textVal):
  markdownPattern = r'(\_\_)([^\_]*)(\_\_)'
  returnText = re.sub(markdownPattern, processItalicMatch, textVal)
  return returnText


def processBoldMatch(matchObj):
  rawText = matchObj.group(0)

  return '<b>' + rawText.replace('**', '') + '</b>'

def processItalicMatch(matchObj):
  rawText = matchObj.group(0)

  return '<i>' + rawText.replace('__', '') + '</i>'
