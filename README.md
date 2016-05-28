# smokeping-target-config-generator
The Python script can convert the raw IP addresses list to SmokePing Target section format so you can append to the SmokePing Target configuration file.

Read raw data named target_IP_list.txt

	aaa.bbb.ccc.ddd

Output as

	  ++ aaa_bbb_ccc_ddd
	  
	  menu = aaa.bbb.ccc.ddd
	  
	  title = aaa.bbb.ccc.ddd
	  
	  host = aaa.bbb.ccc.ddd
	  
	  #alerts = someloss
