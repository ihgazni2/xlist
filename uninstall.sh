pip3 uninstall xlist
git rm -r dist
git rm -r build
git rm -r xlist.egg-info
rm -r dist
rm -r build
rm -r xlist.egg-info
git add .
git commit -m "remove old build"

