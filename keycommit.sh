#
# KeyCommit
# @author: Adrian K Vatchinsky
# @description: Git-Hook to detect and warn users of
# potential security credentials being being commited.

# Populate this with git hook
commit=$1

# Debug print statement
echo "snippet:"
echo "$commit"

# Pipe the commit to the parser
python "$PWD/parser/parser.py"

exit 0