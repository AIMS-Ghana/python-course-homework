gs=$(git status -s)
if [[ $gs ]]
then
  git add --u
  git commit -m "$1"
fi
git push
