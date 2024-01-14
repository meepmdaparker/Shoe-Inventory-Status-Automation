This notebook is a script I created to analyze the status of shoe styles in inventory. The if loop looks through different variations of what kind of style a SKU is, and then identifies which size scale to assess the SKU on. If there are missing inventory of the size scale, then it returns in a new column it's status, which I have named "broken". 


This automates work that would normally take an allocator 30 minutes to an hour; instead of filtering through SKUs by hand, I've drastically shortened the process and made it much more precise. Human error could easily mislabel the status of a shoe.


Additionally, the script can be changed in accordance to the preferences of how one may define a broken or non-shippable style. 
