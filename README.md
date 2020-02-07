# NCSU GIS 714 Spring 2020: Tangible Landscape

![CI](https://github.com/ncsu-geoforall-lab/gis714-2020-tangible-landscape/workflows/CI/badge.svg)

## How to add a new activity

To add a new activity to this project, you need to fork this repository, create a branch, create a pull request,
and of course develop your new activity. The following sections go over the specific steps.
A later section discusses how to modify an action later on using another pull request.

### Set up your repository

To be able to create pull request, you will need to set up a fork and a local repository on your computer
(to make changes and to test code locally):

1. Fork this repository on GitHub.
   * In the web interface, there is a *Fork* button.
1. Clone your fork on your computer.
   * For example, in the command line, use the `git clone` commmand.

### Develop new analysis

1. Create a new Python script according to the template
   * There is a template called `activity_template.py` in the `activities` directory
     which gives information about the specific conventions.
   * Use a unique filename, for example your name or your unique algorithm name.
   * You can use the Simple Python Editor in GRASS GIS.
1. Develop a new analysis and write it as a function in the file.
1. Test your analysis locally on your computer by executing the script.
   * Use the NC SPM sample location for GRASS GIS.
   * If you are using the Simple Python Editor, just run it from there.

### Configure an activity

1. Create a new configuration file according to the template
   * There is a template called `config_template.json` in the `activities` directory
     which provides an example of a minimalistic activity configuration.
   * Again, use a unique filename.
1. Set `analyses` value to the filename of your Python script.
1. Change `title` of the task and modify `layers` to fit your needs.

### Create a pull request

Once you have your new files ready, you can do all the Git related steps
(you could do them as your are working, too).
We will use command line here, but you can use any Git desktop tool including GitHub Desktop.

Create a new branch for your chaneges and switch to it (here, we will call it `add-awesome-activity`):

```
git checkout -b add-awesome-activity
```

Add Python script with your function and the JSON file to the repository as new files:

```
git add activities/awesome-activity.py
git add activities/awesome-activity.json
```

Record the changes:

```
git commit -am "Add awesome activity"
```

Publish the changes into your fork
(`origin` is how Git referes to the remote repository you cloned from,
`add-awesome-activity` is the name of the branch we have picked earlier):

```
git push origin add-awesome-activity
```

This will give your URL to create pull request on GitHub
or simply go to GitHub and it will suggest you to open a PR.

## How to modify your activity

### Update your fork

Modifying your activity, once it was merged into the main repository, requires you to update your fork first.
However, to do that, you need to add the main repository as another remote repository to the clone on your local machine.

So, first, we add the main repository as another remote repository called `upstream`

```
git remote add upstream https://github.com/ncsu-geoforall-lab/gis714-2020-tangible-landscape
```

Second, switch to the master branch of your repository
(the master branch should have no changes in it since you used a separate branch to make the changes):

```
git checkout master
```

Third, update the master branch of your local repository to match the master branch from the main repository
with these two commands:

```
git fetch upstream
git rebase upstream/master
```

Optionally, you can push the update to your remote repository, i.e., your fork on GitHub:

```
git push
```

### Make and publish chnages

Now when your local master branch is up to date with the master branch of the main repository,
you can just follow the instructions above for creating a new activity, in short, you need to:

1. create a new branch (you can do it also after you make the changes),
1. make changes,
1. make commits,
1. publish (push) the changes online, and
1. create a pull request.
