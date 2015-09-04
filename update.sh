git stash save
git fetch origin master
git merge origin/master --ff --no-edit
git stash apply