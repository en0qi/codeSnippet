import csv
import datetime
import os
def main():
	samplename=input("Sample Name:")
	opename=input("Operator Name:")
	CTsize=input("CT視野サイズ[mm]:")
	MATsize=input("マトリクスサイズ:")
	pitch_width=input("ピッチ幅・スライス幅[mm]:")
	skip_voxel=input("スキップボクセル:")
	vol_cube=input("Volume of cube(切り出したい体積の１辺の長さ[mm])")
	now = datetime.datetime.now()
	today = now.strftime("%y%m%d")
	# voxel size
	x = (float(CTsize) / float(MATsize))*(float(skip_voxel)+1.0)
	y = x
	z = float(pitch_width)*(float(skip_voxel)+1.0)
	voxel_number_XY = int(float(vol_cube)/float(x))
	voxel_number_Z = int(float(vol_cube)/float(z))
	print("\n----------------\nVoxel Size\nx:{0}[mm]\ny:{0}[mm]\nz:{1}[mm]\nVoxelNumbers:\nx:{2}\ny:{2}\nz:{3}".format(x,z,voxel_number_XY,voxel_number_Z))
	histmin=input("histmin:")
	histmax=input("histmax:")
	regionXmin=input("Region of Interest\nx_min:")
	regionXmax=int(regionXmin)+voxel_number_XY
	print("x_max:{}".format(regionXmax))
	regionYmin=input("Region of Interest\ny_min:")
	regionYmax=int(regionYmin)+voxel_number_XY
	print("y_max:{}".format(regionYmax))
	regionZmin=input("Region of Interest\nz_min:")
	regionZmax=int(regionZmin)+voxel_number_Z
	print("z_max:{}".format(regionZmax))
	#array2d = [("試料情報",samplename),("解析日",today),("解析者",opename),("CT視野サイズ[mm]",CTsize),("マトリクスサイズ",MATsize),("ピッチ幅•スライス幅[mm]",pitch_width),("Volume of Cube[mm^3]",vol_cube),("x[mm]",x),("y[mm]",y),("z[mm]",z),("histmin",histmin),('histmax',histmax)]
	os.system("touch ./VR_{}_{}.txt".format(today,samplename))
	f = open('./VR_{}_{}.txt'.format(today,samplename),'w')
	f.write("試料情報:"+samplename+"\n解析日:"+today+"\n解析者:"+opename+"\n----------------\nCT視野サイズ:"+CTsize+"[mm]\nスキップボクセル"+skip_voxel+"\nマトリクスサイズ:{0}*{0}\nピッチ幅,スライス幅:{1}[mm]\nvolume of cube:{2}[mm^3]\n----------------\nx:{3}[mm]\ny:{3}[mm]\nz:{4}[mm]\n----------------\nVoxelNumbers:\nx:{5}\ny:{5}\nz:{6}\n----------------\nDataRange:{7} ~ {8}\nRegion of Interest:\nx:{9}~{10}\ny:{11}~{12}\nz:{13}~{14}".format(MATsize,pitch_width,vol_cube,x,z,voxel_number_XY,voxel_number_Z,histmin,histmax,int(regionXmin),regionXmax,int(regionYmin),regionYmax,int(regionZmin),regionZmax))

	f.close()

if __name__ == '__main__':
	main()
