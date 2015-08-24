gs=$(git status -s)
if [[ $gs ]]
then
  git add --u
  git commit -m "$*"
fi
git push
