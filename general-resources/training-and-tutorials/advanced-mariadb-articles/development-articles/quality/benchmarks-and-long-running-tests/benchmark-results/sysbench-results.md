
# Sysbench Results

Results from various Sysbench runs. The data is in OpenDocument Spreadsheet format (.ods).


For reference, the "perro" and "work" systems were configured as follows:



| perro | work |
| --- | --- |
| perro | Linux openSUSE 11.1 (x86_64), single socket dual-core Intel 3.2GHz. with 1MB L2 cache, 2GB RAM, data_dir on 2 disk software RAID 0 |
| work | Linux openSUSE 11.1 (x86_64), dual socket quad-core Intel 3.0GHz. with 6MB L2 cache, 8 GB RAM, data_dir on single disk. |



## sysbench v0.5 results


* Single Five Minutes Runs on T500 Laptop, OO.org spreadsheet: [Sysbench_five_minutes_mariadb_mysql_t500.ods](https://askmonty.org/sysbench-results/Sysbench_five_minutes_mariadb_mysql_t500.ods)


* Single Five Minutes Runs on perro, OO.org spreadsheet: [Sysbench_five_minutes_mariadb_mysql_perro.ods](https://askmonty.org/sysbench-results/Sysbench_five_minutes_mariadb_mysql_perro.ods)


* Single Five Minutes Runs on work, OO.org spreadsheet: [Sysbench_five_minutes_mariadb_mysql_work.ods](https://askmonty.org/sysbench-results/Sysbench_five_minutes_mariadb_mysql_work.ods)


* Three Times Five Minutes Runs on work with 5.1.42, OO.org spreadsheet: [Sysbench_five_minutes_mariadb_mysql_work_5.1.42.ods](https://askmonty.org/sysbench-results/Sysbench_five_minutes_mariadb_mysql_work_5.1.42.ods)


* Three Times Five Minutes Runs on work with 5.2-wl86 key_cache_partitions on and off, OO.org spreadsheet: [Sysbench_five_minutes_mariadb-5.2-wl86_key_cache_partitions_on_off_work.ods](https://askmonty.org/sysbench-results/Sysbench_five_minutes_mariadb-5.2-wl86_key_cache_partitions_on_off_work.ods)


* Three Times Five Minutes Runs on work with 5.1 vs. 5.2-wl86 key_cache_partitions off, OO.org spreadsheet: [Sysbench_five_minutes_mariadb-5.2-wl86_key_cache_partitions_on_off_work.ods](https://askmonty.org/sysbench-results/Sysbench_five_minutes_mariadb-5.1_5.2-wl86_key_cache_partitions_off_work.ods)


* Three Times Fifteen Minutes Runs on perro with 5.2-wl86 key_cache_partitions off, 8, and 32 and key_buffer_size 400, OO.org spreadsheet: [Sysbench_fifteen_minutes_mariadb-5.2-wl86_key_cache_partitions_off_8_32_kbs_400.ods](https://askmonty.org/sysbench-results/Sysbench_fifteen_minutes_mariadb-5.2-wl86_key_cache_partitions_off_8_32_kbs_400.ods)


* Three Times Fifteen Minutes Runs on perro with 5.2-wl86 key_cache_partitions off, 8, and 32 and key_buffer_size 75, OO.org spreadsheet: [Sysbench_fifteen_minutes_mariadb-5.2-wl86_key_cache_partitions_off_8_32_kbs_75.ods](https://askmonty.org/sysbench-results/Sysbench_fifteen_minutes_mariadb-5.2-wl86_key_cache_partitions_off_8_32_kbs_75.ods)


* select_random_ranges and select_random_points, OO.org spreadsheet: [Sysbench_select_random_ranges_points.ods](https://askmonty.org/sysbench-results/Sysbench_select_random_ranges_points.ods)


* select_100_random_points.lua result on perro with key_cache_partitions off and 32, OO.org spreadsheet: [Sysbench_v0.5_select_100_random_points.ods](https://askmonty.org/sysbench-results/Sysbench_v0.5_select_100_random_points.ods)


* `select_random_points.lua --random-points=50` result on perro with key_cache_partitions off and 32, OO.org spreadsheet: [Sysbench_v0.5_select_50_random_points.ods](https://askmonty.org/sysbench-results/Sysbench_v0.5_select_50_random_points.ods)


* `select_random_points.lua --random-points=10` result on perro with key_cache_partitions off and 32, OO.org spreadsheet: [Sysbench_v0.5_select_10_random_points.ods](https://askmonty.org/sysbench-results/Sysbench_v0.5_select_10_random_points.ods)


* `select_random_points.lua --random-points=10, 50, and 100` results on perro with key_cache_segments off, 32, and 64 OO.org spreadsheet: [Sysbench_v0.5_select_random_points_10_50_100_perro.ods](https://askmonty.org/sysbench-results/Sysbench_v0.5_select_random_points_10_50_100_perro.ods)


* `select_random_points.lua --random-points=10, 50, and 100` results on pitbull with key_cache_segments off, 32, and 64 OO.org spreadsheet: [Sysbench_v0.5_select_random_points_10_50_100_pitbull.ods](https://askmonty.org/sysbench-results/Sysbench_v0.5_select_random_points_10_50_100_pitbull.ods)


CC BY-SA / Gnu FDL

