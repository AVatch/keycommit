echo "Hi this is the resolver"
read decision
if [ "$decision" = "yes" ]
then
  echo "user said yes"
elif [ "$decision" = "no" ]
then
  echo "user said no"
fi

exit 0