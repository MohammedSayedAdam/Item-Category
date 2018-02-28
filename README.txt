How to run it
1-Install vagrant and git in your machine
2-Change directory to which you download these files in.
3-You should first run vagrant up and vagrant ssh
3-Go to vagrant folder or shared files and put the download files
4-Create db run this command "python database_setup.py"and run "python filldb.py"
5-Run the project "python fourth.py"
6-Look at the localhost:5000

Endpoints
  the project has 3 json endpoints:
 1-/categories/JSON - list all categories-
 2-/catalog/<int:category_id>/JSON - list            items from a category
3-/catalog/item/<int:item_id>/JSON - show the item details