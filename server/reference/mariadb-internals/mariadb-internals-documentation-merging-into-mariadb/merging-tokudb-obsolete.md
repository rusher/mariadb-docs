
# Merging TokuDB (obsolete)

**Note:** This page is obsolete. The information is old, outdated, or otherwise currently incorrect. We are keeping the page for historical reasons only. **Do not** rely on the information in this article.



We merge TokuDB from Tokutek **git** repositories on GutHub:


* [tokudb-engine](https://github.com/Tokutek/tokudb-engine)
* [ft-index](https://github.com/Tokutek/ft-index)


Just merge normally at release points (use tag names) and don't forget to update `storage/tokudb/CMakeLists.txt`, setting `TOKUDB_VERSION` correctly.

