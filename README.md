Caracal-Site
============

Default Caracal site with predefined Vagrantfile for easy start.

### Preparation

Branch `master` of this repository should only be used for improving development environment files. For regular site development it is paramount that you create your own branch. That said, the following steps need to be executed in order to get a new fully functional development environment for Caracal-based site:

* [Create a new empty repository](https://github.com/repositories/new) on GitHub. This is where we will keep site-specific files, so name it according to site. For the sake of tutorial we'll call it `New-Site`;
* Clone new repository to your local machine under `New-Site` name by issuing the following command:
```
git clone git@github.com:You/New-Site.git New-Site
```
* Go in to `New-Site` directory;
* We need to add [Caracal-Site](https://github.com/Way2CU/Caracal-Site) as `upstream` so Git knows where to pull things from. You do that with following command:
```
git remote add upstream https://github.com/Way2CU/Caracal-Site.git
```
* We need to get `upstream` data. To do that issue the following command;
```
git pull upstream master
```
* Our new repository is ready, we can now push changes to GitHub:
```
git push origin --all
```

### Development environment

We use Vagrant to set up our environment. Once preparation is done you will have couple of files in your `New-Site` directory. These files should not be changed. While in `New-Site` directory issue the following command:
```
vagrant up
```
This should download, prepare and configure development environment for `New-Site`. This preparation can take a while depending on your network speed. Once preparation is done, additional files will appear in your directory. You can now start working on your new project.

Suspending virtual environment is done with `vagrant suspend` and resumed with `vagrant resume`. Once development is completed virtual environment can be destroyed with `vagrant destroy` without affecting site files.
