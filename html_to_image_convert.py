from html2image import Html2Image

hti = Html2Image()

hti.screenshot(url='https://www.python.org', save_as='python_org.png', size=(2000, 2500))  # size (width,height)
