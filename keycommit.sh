#!/bin/sh
#
# KeyCommit
# @author: Adrian K Vatchinsky
# @description: Git-Hook to detect and warn users of
# potential security credentials being being commited.

# Populate this with git hook
# commit=$1
commit=`git diff`
# Debug print statement
# echo "snippet:"
# echo "$commit"

# Pipe the commit to the parser
python "$PWD/keycommit.py" "$commit"
# Pipe decision to resolver
if [ ! -f tmp.txt ]; then
    exit 0
else
    # pipe decision to resolver
    less "tmp.txt" | ./resolver.sh
    # Clean up
    rm "tmp.txt"
fi
exit 0