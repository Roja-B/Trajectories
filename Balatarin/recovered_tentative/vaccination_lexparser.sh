/media/data3/roja/Vaccination/stanford-parser-2012-03-09/lexparser.sh
3210
#"! 
 -outputFormat "typedDependencies" edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz $*
java -mx1000m -cp "$scriptdir/*:" edu.stanford.nlp.parser.lexparser.LexicalizedParser \
scriptdir=`dirname $0`
  exit
  echo
  echo Usage: `basename $0` 'file(s)'
if [ ! $# -ge 1 ]; then
# Runs the English PCFG parser on one or more files, printing trees only
#!/usr/bin/env bash

