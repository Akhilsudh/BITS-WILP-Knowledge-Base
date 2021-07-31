# BITS-WILP-Knowledge-Base
Welcome to my BITS WILP Knowledge Base. This is a personal note book for all the notes I take as part of my journey here at BITS. To know more about what a knowledge base is check [this](https://en.wikipedia.org/wiki/Knowledge_base) out.

## So what is the purpose of this? 🤷🏽‍♂️
My learning method includes taking a lot of notes through a local note taking tool called [Obsidian](https://obsidian.md/). This website simply hosts that vault of Obsidian notes. The purpose of this page is to make the notes taken throughout my coursework accessible to myself and others in the same boat as me. Maybe this can help you too 🤘🏽
To know more about Obsidian and what it is, you can read about it in my blog article [here](https://justanothergeek.hashnode.dev/obsidian-as-a-second-brain)

## Usage
### Deploy to Github Pages
1. Fork this repository 
2. Add your documents to `docs` , `docs/index.md` is the main page of the website
3. Open `mkdocs.yml`, modify `site_name` to your website name, this file is the configuration file for the website, visit links below to know more:
    * [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)
    * [mkdocs](https://www.mkdocs.org/user-guide/configuration/)
4. Push to github, 
5. Go to github setting, open github page, choose `gh-pages` branch, wait a moment, then visit `https://<your-github-username.github.io/<your-repo>`, for example:`https://akhilsudh.github.io/BITS-WILP-Knowledge-Base/`

Thnks to `Github Actions`, it is easy to deploy a static page, all you need to do is modify and push your changes and the actions defined in the repo will deploy the page for you in the `gh-pages` branch

### Deploy Locally
1. The simplest way: Enter your local repo directory, make sure your python > 3.6
    ```
    pip install -r requirements.txt
    mkdocs serve 
    ```
2. Then visit `http://127.0.0.1:8000/`