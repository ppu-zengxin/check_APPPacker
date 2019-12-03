import zipfile
import sys

#@Time    :2019.12.3
#@Author  :zengxin

packer_dict={
	"libchaosvmp.so":"使用了娜迦进行加固",
	"libddog.so":"使用了娜迦进行加固",
	"libfdog.so":"使用了娜迦进行加固",
	"libedog.so":"使用了娜迦企业版进行加固",
	"libexec.so":"使用了爱加密加固（可能性大）或腾讯进行加固",
	"libexecmain.so":"使用了爱加密进行加固",
	"ijiami.dat":"使用了爱加密进行加固",
	"ijiami.ajm":"使用了爱加密企业版进行加固",
	"af.bin":"使用了爱加密进行加固",
	"signed.bin":"使用了爱加密进行加固",
	"libsecexe.so":"使用了梆梆免费版进行加固",
	"libsecmain.so":"使用了梆梆免费版进行加固",
	"libSecShell.so":"使用了梆梆免费版进行加固",
	"secData0.jar":"使用了梆梆免费版进行加固",
	"libSecShell-x86.so":"使用了梆梆免费版进行加固",
	"libDexHelper.so":"使用了梆梆企业版进行加固",
	"libDexHelper-x86.so":"使用了梆梆企业版进行加固",
	"classes.jar":"使用了梆梆定制版进行加固",
	"DexHelper.so":"使用了梆梆定制版进行加固",
	"libprotectClass.so":"使用了360进行加固",
#	".appkey":"使用了360进行加固",
	"libjiagu.so":"使用了360进行加固",
	"libjiagu_art.so":"使用了360进行加固",
	"libjiagu_x86.so":"使用了360进行加固",
	"libcmvmp.so":"使用了中国移动安全进行加固",
	"libmogosec_dex.so":"使用了中国移动安全进行加固",
	"libmogosec_sodecrypt.so":"使用了中国移动安全进行加固",
	"libmogosecurity.so":"使用了中国移动安全进行加固",
	"mogosec_classes":"使用了中国移动安全进行加固",
	"mogosec_data":"使用了中国移动安全进行加固",
	"mogosec_dexinfo":"使用了中国移动安全进行加固",
	"mogosec_march":"使用了中国移动安全进行加固",
	"libegis.so":"使用了通付盾进行加固",
	"libNSaferOnly.so":"使用了通付盾进行加固",
	"libreincp.so":"使用了珊瑚灵御进行加固",
	"libreincp_x86.so":"使用了珊瑚灵御进行加固",
	"libnqshield.so":"使用了网秦进行加固",
	"libbaiduprotect.so":"使用了百度进行加固",
	"baiduprotect1.jar":"使用了百度进行加固",
	"baiduprotect.jar":"使用了百度进行加固",
	"libuusafe.jar.so":"使用了UU安全进行加固",
	"libuusafe.so":"使用了UU安全进行加固",
	"libuusafeempty.so":"使用了UU安全进行加固",
	"dp.arm-v7.so.dat":"使用了DexProtect进行加固",
	"dp.arm.so.dat":"使用了DexProtect进行加固",
	"aliprotect.dat":"使用了阿里聚安全进行加固",
	"libsgmain.so":"使用了阿里聚安全进行加固",
	"libsgsecuritybody.so":"使用了阿里聚安全进行加固",
	"libmobisec.so":"使用了阿里聚安全进行加固",
	"libfakejni.so":"使用了阿里聚安全进行加固",
	"libzuma.so":"使用了阿里聚安全进行加固",
	"libzumadata.so":"使用了阿里聚安全进行加固",
	"libpreverify1.so":"使用了阿里聚安全进行加固",
	"classes.dex.dat":"使用了dexprotect进行加固",
	"dp.arm-v7.so.dat":"使用了dexprotect进行加固",
	"dp.arm.so.dat":"使用了dexprotect进行加固",
	"libtup.so":"使用了腾讯进行加固",
	"libshell.so":"使用了腾讯进行加固",
	"tencent_stub":"使用了腾讯进行加固",
	"mix.dex":"使用了腾讯进行加固",
	"libshella":"使用了腾讯进行加固",
	"libshellx":"使用了腾讯进行加固",
	"libshella-xxxx.so":"使用了腾讯进行加固",
	"libshellx-xxxx.so":"使用了腾讯进行加固",
	"mix.dex":"使用了腾讯进行加固",
	"mixz.dex":"使用了腾讯进行加固",
	"libtosprotection.armeabi.so":"使用了腾讯御安全进行加固",
	"libtosprotection.armeabi-v7a.so":"使用了腾讯御安全进行加固",
	"libtosprotection.x86.so":"使用了腾讯御安全进行加固",
	"libtest.so":"使用了腾讯御安全进行加固",
	"tosversion":"使用了腾讯御安全进行加固",
	"libTmsdk":"使用了腾讯御安全进行加固",
	"libTmsdk-xxx-mfr.so":"使用了腾讯御安全进行加固",
	"libnesec.so":"使用了网易易盾进行加固",
	"libAPKProtect.so":"使用了APKProtect进行加固",
	"libkwscmm.so":"使用了几维安全进行加固",
	"libkwscr.so":"使用了几维安全进行加固",
	"libkwslinker.so":"使用了几维安全进行加固",
	"kdpdata.so":"使用了几维安全进行加固",
	"dex.dat":"使用了几维安全进行加固",
	"libkdp.so":"使用了几维安全进行加固",
	"libx3g.so":"使用了顶像科技进行加固",
	"libapssec.so":"使用了盛大进行加固",
	"librsprotect.so":"使用了瑞星进行加固",
	"libitsec.so":"使用了海云安进行加固",
	"itse":"使用了海云安进行加固",
	"libapktoolplus_jiagu.so":"使用了apktoolplus进行加固",
	"jiagu_data.bin":"使用了apktoolplus进行加固",
	"sign.bin":"使用了apktoolplus进行加固"
}

def packerDetector(apkpath):
	packertype="未进行加固或未匹配到该特征库"
	packersign=""
	zipfiles=zipfile.ZipFile(apkpath)
	nameList=zipfiles.namelist()
	for fileName in nameList:
		for packer in packer_dict.keys():
			if packer in fileName:
				packertype=packer_dict[packer]
				packersign=packer
	print("经检测，该apk"+packertype)

def main():
    if len(sys.argv)==2:
        packerDetector(sys.argv[1])
    else:
        print("请输入正确的apk包名")
        print("eg:python3 check_APPPacker.py whm_2019.apk")

if __name__ == '__main__':
    main()
