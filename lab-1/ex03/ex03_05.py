def dem_so_lan_xuat_hien(lst):
    count_dirct ={}
    for item in lst:
        if item in count_dirct:
            count_dirct[item] +=1
        else:
            count_dirct[item] =1
    return count_dirct
input_string = input("Nhap danh sach tu, cach nhau bang dau cach: ")
world_list = input_string.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(world_list)
print("so lan xuat hien cua cac phan tu: ",so_lan_xuat_hien)
