<<<<<<< Updated upstream
git stash save
git fetch origin master
git merge origin/master --no-edit
git stash apply
=======
git fetch origin master
git merge origin/master --ff --no-edit
>>>>>>> Stashed changes
