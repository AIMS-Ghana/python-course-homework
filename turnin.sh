gs=$(git status -s)
if [[ $gs ]]
then
  git add --u
  git commit -m "$*"
  git push
else
  echo "no changes to turnin!"
fi
