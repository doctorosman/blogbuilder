import os, shutil, codecs

POSTS = []

def config(theme, blog_title, page_title, pp_file_path, footer):
    global BLOG_TITLE, PAGE_TITLE, PP_FILE_PATH, FOOTER, THEME
    BLOG_TITLE = blog_title
    PAGE_TITLE = page_title
    PP_FILE_PATH = pp_file_path
    THEME = "themes/" + theme
    FOOTER = footer

def post(path_name, title, image_file_path, summary, content):
    global POSTS, THEME
    doc = open(THEME + "/post.div", "r")
    POSTS.append(doc.read().format(post_link = "posts/" + path_name, post_img_file = image_file_path, post_title = title, post_summary = summary))
    doc.close()

def copytree(src, dst, symlinks=False, ignore=None):
    shutil.rmtree(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def build():
    global BLOG_TITLE, PAGE_TITLE, PP_FILE_PATH, FOOTER, THEME, POSTS
    source = THEME + "/"
    if not os.path.exists("output"):
        os.makedirs("output")
    target = "output/"
    copytree(source, target)

    doc = open(THEME + "/index.html", "r")
    new = codecs.open("output/index.html", "w", "utf-8")
    divs = ""
    for post in POSTS:
        divs += post + "\n"
    new.write(doc.read().format(page_title = PAGE_TITLE, pp_file = PP_FILE_PATH, blog_title = BLOG_TITLE, posts = divs, footer = FOOTER))
    doc.close()
    new.close()
