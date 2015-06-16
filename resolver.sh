echo "Hi this is the resolver"
read decision
if [ "$decision" = "yes" ]
then
  echo "user said yes"
  exit 1
elif [ "$decision" = "no" ]
then
  echo "user said no"
  exit 0
fi

exit 0