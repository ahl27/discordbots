#!/bin/bash

echo -e "\033[0;32mDeploying addresses to GitHub...\033[0m"

git add .

# Commit changes.
msg="adding new addresses `date`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"

# Push source and build repos.
git push 

