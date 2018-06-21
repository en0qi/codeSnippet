import csv
import datetime
import os
def main():
	samplename=input("Sample Name:")
	opename=input("Operator Name:")
	CTsize=input("CT視野サイズ[mm]:")
	MATsize=input("マトリクスサイズ:")
	pitch_width=input("ピッチ幅・スライス幅[mm]:")
	vol_cube=input("Volume of cube(切り出したい体積[mm^3])")
	now = datetime.datetime.now()
	today = now.strftime("%y%m%d")
	x = float(CTsize) / float(MATsize)
	y = x
	z = float(pitch_width)
	voxel_size = x*y*z
	voxel_number = float(vol_cube) / float(voxel_size)
	print("\n----------------\nx:{0}[mm]\ny:{0}[mm]\nz:{1}[mm]".format(x,z))
	histmin=input("histmin:")
	histmax=input("histmax:")
	
	#array2d = [("試料情報",samplename),("解析日",today),("解析者",opename),("CT視野サイズ[mm]",CTsize),("マトリクスサイズ",MATsize),("ピッチ幅•スライス幅[mm]",pitch_width),("Volume of Cube[mm^3]",vol_cube),("x[mm]",x),("y[mm]",y),("z[mm]",z),("histmin",histmin),('histmax',histmax)]
	os.system("touch ./VR_{}_{}.txt".format(today,samplename))
	f = open('./VR_{}_{}.txt'.format(today,samplename),'w')
	f.write("試料情報:"+samplename+"\n解析日:"+today+"\n解析者:"+opename+"\n----------------\nCT視野サイズ:"+CTsize+"[mm]\nマトリクスサイズ:{0}*{0}\nピッチ幅,スライス幅:{1}[mm]\nvolume of cube:{2}[mm^3]\n----------------\nx:{3}[mm]\ny:{3}[mm]\nz:{4}[mm]\nDataRange:{5} ~ {6}".format(MATsize,pitch_width,vol_cube,x,z,histmin,histmax))

	f.close()

if __name__ == '__main__':
	main()
