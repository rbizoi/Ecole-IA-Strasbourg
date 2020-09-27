repGitHub=https://raw.githubusercontent.com/rbizoi/Spark-developper-pour-le-Big-Data/master/donnees/brazilian_e-commerce

wget $repGitHub/olist_closed_deals_dataset.csv
wget $repGitHub/olist_customers_dataset.zip
wget $repGitHub/olist_geolocation_dataset.zip
wget $repGitHub/olist_marketing_qualified_leads_dataset.csv
wget $repGitHub/olist_orders_dataset.zip
wget $repGitHub/olist_order_items_dataset.zip
wget $repGitHub/olist_order_payments_dataset.zip
wget $repGitHub/olist_order_reviews_dataset.zip
wget $repGitHub/olist_products_dataset.zip
wget $repGitHub/olist_sellers_dataset.csv
wget $repGitHub/product_category_name_translation.csv

unzip -o olist_customers_dataset.zip      && rm olist_customers_dataset.zip     
unzip -o olist_geolocation_dataset.zip    && rm olist_geolocation_dataset.zip   
unzip -o olist_order_items_dataset.zip    && rm olist_order_items_dataset.zip   
unzip -o olist_order_payments_dataset.zip && rm olist_order_payments_dataset.zip
unzip -o olist_order_reviews_dataset.zip  && rm olist_order_reviews_dataset.zip
unzip -o olist_orders_dataset.zip         && rm olist_orders_dataset.zip        
unzip -o olist_products_dataset.zip       && rm olist_products_dataset.zip      

hdfs dfs -mkdir donnees/e-commerce
hdfs dfs -moveFromLocal *.csv donnees/e-commerce
hdfs dfs -ls donnees/e-commerce

hdfs dfs -rm -R -f -skipTrash donnees/e-commerce
