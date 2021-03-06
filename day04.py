#adventofcode2017
#crushallhumans
#day4
#20171204


#part 1 = no duplicate words

import re
import itertools

re_compiled = re.compile('\s+')

def no_duplicates(i):
    global re_compiled
    words = re_compiled.split(i)
    counts = {}
    rounds = 0

    # first pass, easy
    for ii in words:
        if ii in counts:
            print '{} BAD WORD, {} duped after {} rounds'.format(i,ii,rounds)
            #print '{} BAD ANAGRAM, {} duped'.format(counts,j)
            return False
        else:
            counts[ii] = True

    # second pass, hard
    for ii in words:
        anagrams = 0
        # permutations are by position, not value
        # so 'kvvlf' will self-duplicate in the permutation set
        inner_dupes = {}
        for jj in itertools.permutations(ii,len(ii)):
            j = ''.join(str(s) for s in jj)
            if j != ii and j not in inner_dupes:
                inner_dupes[j] = True
                if j in counts:
                    #print '{} BAD, {} duped'.format(words,ii)
                    print '{} BAD ANAGRAM, {} duped after, {} rounds, {} anagrams'.format(i,j,rounds,anagrams)
                    return False
                else:
                    counts[j] = True
            anagrams += 1
        rounds += 1
    return True

test_set = []
test_set.append(['aa bb cc dd ee',True])
test_set.append(['aa bb cc dd aa',False])
test_set.append(['aa bb cc dd aaa',True])

#for i in test_set:
#    assert (no_duplicates(i[0]) == i[1])

puzzle_set = []
puzzle_set.append('kvvfl kvvfl olud wjqsqa olud frc')
puzzle_set.append('slhm rdfm yxb rsobyt rdfm')
puzzle_set.append('pib wzfr xyoakcu zoapeze rtdxt rikc jyeps wdyo hawr xyoakcu hawr')
puzzle_set.append('ismtq qwoi kzt ktgzoc gnxblp dzfayil ftfx asscba ionxi dzfayil qwoi')
puzzle_set.append('dzuhys kfekxe nvdhdtj hzusdy xzhehgc dhtvdnj oxwlvef')
puzzle_set.append('gxg qahl aaipx tkmckn hcsuhy jsudcmy kcefhpn kiasaj tkmckn')
puzzle_set.append('roan kqnztj edc zpjwb')
puzzle_set.append('yzc roc qrygby rsvts nyijgwr xnpqz')
puzzle_set.append('jqgj hhgtw tmychia whkm vvxoq tfbzpe ska ldjmvmo')
puzzle_set.append('nyeeg omn geyen ngyee rcjt rjuxh')
puzzle_set.append('qpq udci tnp fdfk kffd eyzvmg ufppf wfuodj toamfn tkze jzsb')
puzzle_set.append('rrcgxyp rbufd tfjmok vpyhej hcnz ftkojm')
puzzle_set.append('jnmomfc jnmomfc bkluz izn ovvm flsch bkluz')
puzzle_set.append('odisl hzwv hiasrhi hez ihihsra qpbmi ltwjj iknkwxf nbdtq gbo')
puzzle_set.append('gjtszl gjtszl fruo fruo')
puzzle_set.append('rdapv gaik cqboix sxnizhh uxmpali jdd usqnz advrp dze')
puzzle_set.append('flooz flooz qad tcrq yze bnoijff qpqu vup hyagwll')
puzzle_set.append('lnazok dze foi tqwjsk hpx qcql euzpj mwfrk')
puzzle_set.append('ilb fmviby ivybmf gtx xtg')
puzzle_set.append('rpauuu timere gyg wcolt ireetm safi')
puzzle_set.append('croe szwmq bbhd lciird vhcci pdax')
puzzle_set.append('hnc ykswt qqqmei goe bri wmyai hnc qpgqc pberqf bzs')
puzzle_set.append('hsnrb wdvh iezzrq iezzrq rdbmpta iezzrq kemnptg alkjnp wymmz')
puzzle_set.append('ngw don ddvyds nlhkoa aaf gptumum ugtpmmu')
puzzle_set.append('vmccke qbpag kvf kvf tgrfghb kvf bhpd sglgx')
puzzle_set.append('obomgk bkcgo yso ttft vbw ckl wjgk')
puzzle_set.append('fli qvw zhin dfpgfjb udsin nihz ovr tiewo')
puzzle_set.append('tgmzmph hauzieo jmg tdbtl lvfr qpaayq qapaqy ausioeu jun piygx')
puzzle_set.append('jkp guqrnx asdqmxf vmfvtqb tloqgyo ioix gajowri tmek ilc puhipb')
puzzle_set.append('uycn zxqm znft ayal znacus kvcyd ekv qqfpnh')
puzzle_set.append('fqghur xtbtdd ztjrylr bpuikb ziyk')
puzzle_set.append('rvakn uqbl ozitpdh uqbl dsej xehj')
puzzle_set.append('laxp haz jyd xnkrb ijldth woy xapl iqgg alpx gnupa ukptmmh')
puzzle_set.append('dyiy dyiy ihb qcyxr')
puzzle_set.append('wbwkd hdwu zvgkn hdwu wjc sakwhn zxujdo npllzp uyr uyr')
puzzle_set.append('fxczpmn cininu akcxs ggslxr riyxe ojisxe')
puzzle_set.append('ppbch sampq dnct afikor dnct edsqy pnzyzmc afikor')
puzzle_set.append('jnvygtn hijqjxl vsd jnvygtn nqcqv zns odq gkboxrv kolnq wrvd')
puzzle_set.append('mroq mroq flsbu flsbu')
puzzle_set.append('fyshor xvpaunj qmktlo xoce wkiyfu ukcl srndc ugwylwm ozcwdw mtqcste kpokr')
puzzle_set.append('cfh cxjvx cfh cfh uewshh')
puzzle_set.append('bpspbap bpspbap fquj mxmn bwls iirhvuk dmpkyt exrn mxmn')
puzzle_set.append('tvyvzk ezszod ntxr xtnr och')
puzzle_set.append('knfxhy kbnyl knfxhy xhkssx lxru uprh nkxpbx oodolxr tpvyf')
puzzle_set.append('nblmysu iwoffs upgof tyagwf aan vovji ajk ywzq oyfi sfulz')
puzzle_set.append('aushzkm lcaeki mkuzsah ynxvte rsntd refk pcm')
puzzle_set.append('mgguob gobmug dzenpty gmogbu')
puzzle_set.append('yvq eepof rgnree nerger fpb stfrln ernger')
puzzle_set.append('hrgkbl mzwvswk rsrsbk ieru holco pajvvn ztgsr qkyp fyeg owpcmoj')
puzzle_set.append('fowda gmsqdca yugj mcrroxv mqcbojd fjnqfji qdfsc jqs')
puzzle_set.append('qnc rvjfz vvxk sjd xrma ucdjvq sbw zydyt dfzww')
puzzle_set.append('ocajazv cozaajv tqunkla udwf ecnnmbz lsakqg bki njnda zsdu ccfqw rxpc')
puzzle_set.append('qqm qdfya qxyx qmq qfday uqnfttt')
puzzle_set.append('rnbirb iapor qet iapor hxkhz dfvzig pedl ybyb')
puzzle_set.append('mkgamxg xkniv meb hbzmxjn dhbj zhbxjmn hdjb')
puzzle_set.append('ilteux pyutyfx mau lrr bacak')
puzzle_set.append('sjjonmn dbbbgs crxyuu jztstgd ezb uiabyaa')
puzzle_set.append('tra fle ufzlvf nnaw kec hiwnnlj tei wld iyt syk hjdczb')
puzzle_set.append('qmd jtlud dgh dbanock fzp dsjgqru wwvo jwvxwgv xlemfij jcacd')
puzzle_set.append('rpkx oxesil snazcgx fly miiyc ikmtmp oefyyn egbw')
puzzle_set.append('ypfpeu wldnyd acchppb yqwcaw wldnyd turbz megci nbgxq xkc ypfpeu')
puzzle_set.append('iqqv iqqv neui iqqv')
puzzle_set.append('ypsxm icqyup zyetrwq nbisrv')
puzzle_set.append('viommi toszx dpueq eyy cunjou ffcjc jaeez djefra pxvkj liudlig yye')
puzzle_set.append('fhnacbg jghchh ghjhhc iue hwqmo')
puzzle_set.append('vbjw lpn cizba ltnsfpz tzoweml irewlc uzckhpd mszal obd')
puzzle_set.append('yeos utxkft hflxkfe fxczge qpgigkc ksgr vuumql vhlvv')
puzzle_set.append('xzmkv xzmkv krecdi klpem jsbu nwcmik emfzxf cjmpgnj')
puzzle_set.append('vtkjo pmiv zou gxo qdiyxsf hwyinjk jhkgf rjq')
puzzle_set.append('dyuoc ywiyvch irfgl ywiyvch fxb fxb')
puzzle_set.append('tuz onhr syu rqya abkaf bcfx mbknex juwoor zmksl')
puzzle_set.append('oheg spjorx ksdy vwtq fxz phvtazk tcze lrxg')
puzzle_set.append('hew lbup botaj ltr jpd')
puzzle_set.append('dxgc tzinkej gnz hxvvub adsqmc dxgc asgpp rqbdcra goy pmamdua bhiacva')
puzzle_set.append('xqv ygb kihxqz vyv pjcny vmyvsdv cgsi nfyx')
puzzle_set.append('tqga ssshrw ndq qlbvwh huyd pxbgj qbxk dkkbf jxy chsobw pph')
puzzle_set.append('hxl iwph iwph xnr otifm ljhre')
puzzle_set.append('zlgvpd kapxpoc dve rklk ogh hgnp rbrmc zzkz hhmcx aklmo')
puzzle_set.append('sar gfor nkf hek nkf aql shc aql')
puzzle_set.append('dtcrw kfjzcjx qyhi bldson whwdayo mqtgt xhqzp ttqmg')
puzzle_set.append('omspdml isze jdl nvwo qrkm wztfg ssfgyh dryj jhp unsmty')
puzzle_set.append('jxt cszylng ifht ixtuna azoi xutqlv jtx tjx')
puzzle_set.append('usgm azuayp fgkby ezpyq jqwl ezofj')
puzzle_set.append('tnhvil nrvg moyrpqs sldx qymoff megflxh pyhqwms xmdw')
puzzle_set.append('zomy zcquwnv lzx bvcna yods mjp dgsez')
puzzle_set.append('blklyf xokd gpit tiysj yrwfhm tofx')
puzzle_set.append('dtig vhdp omuj vhpd')
puzzle_set.append('fogwxim qvdwig emdiv jvhl euwbzkg xvxb hwmqo ujdmlp epmykj')
puzzle_set.append('sjxll sjxll pedvgb sjxll')
puzzle_set.append('drvay gtzhgtx yrt okz nqf')
puzzle_set.append('haxfazn pvkovwb pgu tgshw mxcjf pbe nwoymzc mxcjf pbe hydwy jradcr')
puzzle_set.append('prjsloa ahylvj okbsj qbdcdjt pmfo pagyoeg vkmhjzt khzmjvt opfm xfrji gyjqyel')
puzzle_set.append('lzypt jdbtrad ogr jdbtrad heink')
puzzle_set.append('rcoucuq gdxewa rcoucuq whlw zhhm rcoucuq azaqohe mzyli rdvaf')
puzzle_set.append('yuag ebcf yuag nsotg qqzuxr jfmao vyucw wmoye')
puzzle_set.append('qwvk xemm hgqrr wyxkpp tojndm xlvzypw jus bgnu bgnu nklfwhs')
puzzle_set.append('daqi knenmku ccm xkiuy vkexsbc kvvdagx umopitw yaocnx yoakqql mllmsp')
puzzle_set.append('mrxgl gywit mfopia ncnsvw vdxek axuiot rsejua nei prndudz mnu')
puzzle_set.append('egqn gaa qgen urs mix zbn rhn')
puzzle_set.append('ewharq aihy udkdaob kgrdd kgrdd kugbjtj fcef llqb pduxaq wcexmm')
puzzle_set.append('dwtiw nelq hppad algxgf gcc upou akm efnb mxmhrud')
puzzle_set.append('yxqaa ups okbhgt iet qns tqn rnjqxgp')
puzzle_set.append('npmhdm cgds ldexvr typi jyivoqk zkgq vfyxu xgfo')
puzzle_set.append('dkwnmr umm dkwnmr okpjw wqx jpztebl eqsib dkwnmr')
puzzle_set.append('dxbild wpbup evscivq dxbild dxbild geqp ojfbpl jshvqej')
puzzle_set.append('cxdntxs csfocjd pyy tuhws teb boyloz xfw scxh pxhonky')
puzzle_set.append('lteucke xrgwy hszgzu hnyrcvb')
puzzle_set.append('pfgsgwg dxzh fworek qbstod')
puzzle_set.append('usemcrf psczxu gcjtr brls')
puzzle_set.append('hjol efxczux bqdn gvrnpey yyoqse gbam ndzyj lbwb bhzn unsezg')
puzzle_set.append('bapw xifz blupk qqdk bofvqpp wnbuwyt rnwocu lzwgtt zucag pov')
puzzle_set.append('xkre lqvd juf lqvd xio xyg xyg')
puzzle_set.append('tzdao ztheib aymcf aorg iyawrch hetcxa iyawrch czdymc ccv')
puzzle_set.append('ucgl azlppu jvxqlj pest')
puzzle_set.append('dvwlw fuuy mnhmm okrp ualnqlm uyuznba fzyejk yaq crl ctprp')
puzzle_set.append('odfq knox mkbcku pxucmuf lpjpol phl')
puzzle_set.append('ixongh hfs ruorbd auy qyssl kykwcix aytsm rlj aytsm duq segpqhk')
puzzle_set.append('izufsk wedpzh podjkor eamo vqvev ifnz podjkor xrnuqe')
puzzle_set.append('twyfps bmdbgtu qye qkwjms')
puzzle_set.append('wlav htym vhsnu cocphsj mdsuq vhsnu jflgmrp')
puzzle_set.append('opajag itwjhfu purnnvk opajag')
puzzle_set.append('hpkopqp vnj aialpt lzrkzfs nwucez nwuezc')
puzzle_set.append('mcx hzcjxq zbxr dsx tpknx fva')
puzzle_set.append('rlvgm xrejsvn ghawxb efyos xty wdzdgh olahbtn rga efyos vhtm nsr')
puzzle_set.append('cni mbab qtgeiow ulttn rckc kmiaju jvbq emyvpew cdlxldn ulttn brhkprx')
puzzle_set.append('eykpffp rapik qki fhjgdyu tome ehjuy bibjk htxd vexvag')
puzzle_set.append('wrk dpxt gwkuiov gbkif ike gbkif pcd wpj toywyf qzsa aol')
puzzle_set.append('yqwzh uujn ujun ujnu')
puzzle_set.append('srs ralwxrz yxvvmgp sjhbhk waasid cqtxoxf whcladv jkmaq khjbsh dlavcwh')
puzzle_set.append('mdvsjh xaj etvxlsy fxgiy rgjesel rlegesj ptriz ebdyhkp kugxm dxv egljser')
puzzle_set.append('lhehwrs mqevb ygmv gri izop qgb ivm')
puzzle_set.append('loqqam alojlwg hgen hbyw qlwpun loqqam worgnwk kope')
puzzle_set.append('phozre todsknr todsknr ibj mvllsar')
puzzle_set.append('wuripy ruwlfbh wukbkey qhq iishw tvtvci xawvxc vxacwx hsiwi ogq')
puzzle_set.append('xryq vxwupqa zhqex aquxpwv bnvxrba dtbxki')
puzzle_set.append('yvvwh zvsm vqskhp vqskhp ggqqlw bpn wbuv')
puzzle_set.append('kqz tdy goqwge ygn jgd')
puzzle_set.append('szjjhdk zkpoo nxexz ebicc')
puzzle_set.append('wzuemcj oyd qupulju iaakzmt vzkvz')
puzzle_set.append('nppahov umm wpzev wxkgfxd owgekp bhhb bbhh dgviiw kdfgxwx wryb')
puzzle_set.append('bnc rhes lmbuhhy kwbefga bnc rtxnvz bnc')
puzzle_set.append('ani mggxf mcoixh zdd nai hbhzl mes bdpqr')
puzzle_set.append('mjn uinoty jjegvze bjgqg yhqsxbt coj obylb hddude xqi rhfbhha alood')
puzzle_set.append('cbjzj drmihy tfkrhsd nuhav hihzx bvblqpl tdd szmp gjgfv box')
puzzle_set.append('uumhdxd cmwgyf vepr rwqdkj exwk')
puzzle_set.append('hwvr ydvw bqefu kghes gvbhp awms iqsqes khgse')
puzzle_set.append('mrey jqfw fwvzhps komj dayvs fbui zmtd cofn mrey')
puzzle_set.append('dsjds fdpx irjj usndok qcctsvf fgk wvg txwxcl dxs llp zyilwtq')
puzzle_set.append('xmkelgk fdukc cye legkxkm wwly')
puzzle_set.append('enlny eynln cccku brkz dpof mwfoxcd yftmnqh wpebvyc')
puzzle_set.append('ggdn jnysl dsacffw ukj hdae cmzxku')
puzzle_set.append('uqhm gcachmn kxndfrl htmfis jfnajz fiqiypr kekho kekho ndcw ckrndub dejfna')
puzzle_set.append('keazuq ertql rauwl keazuq obmh rauwl ksrotm')
puzzle_set.append('jppp poigqhv repfsje grjk xwkyuh pkx ayzcj hoxzv')
puzzle_set.append('yhjw pcuyad icie icie icie hwcsuy wcd yihjh jnrxs')
puzzle_set.append('gaug ivvx ceb xujonak hbtfkeb ttciml cctoz')
puzzle_set.append('dggyyi dggyyi gqlyumf yasu fwdfa cbb nncn verhq')
puzzle_set.append('rhgcw gpcyct kiuhbg kiuhbg gpcyct jlmleo nhumm')
puzzle_set.append('wulxxu jyjek hclcp ogob viex wiqcupq')
puzzle_set.append('tthu nxgzpid kcnj mss ukapgkp nnc bxjocv qwxs oejwsif aywqtu brahkb')
puzzle_set.append('dtde bgvb smu vbbg zhlu')
puzzle_set.append('lyo nwjjmep ldbok wgxhto wwuh qfgjknk wnsl')
puzzle_set.append('lleyr onha hkwulbm jfg')
puzzle_set.append('bybjwd uoxvbh mvj iqfpnxs bybjwd zqtszp wvc lbazjr zkzenja cev')
puzzle_set.append('rbuyyr divtslq yuqmyt ajyveb smxsjb nlk tzqhq ims fewg wpjhr gqh')
puzzle_set.append('kpewfd beq klilis klisli eeezut')
puzzle_set.append('euqh hueq ldoo crqurv lvrwh tmaewp oodl')
puzzle_set.append('bqi lzrf jyhvxfh bqi jyhvxfh nbztd lwpdn cuzi')
puzzle_set.append('srjylou phavzjd wost uxkaq byh sluryoj')
puzzle_set.append('ihrdk bcegkpq nygrs qbcq wyjg dvzme pgzhjl vibg kvv')
puzzle_set.append('ijsx iedemek ktlz gtga tbal lbki gtga')
puzzle_set.append('vmiaxn kefig kefig vngxz')
puzzle_set.append('vrdmfvi qts vlvhq vlvhq dihmq')
puzzle_set.append('cfz dyrz zlw qnt vok fwvahg skshbqf hbwozdc ntana jdb uflp')
puzzle_set.append('rimbj bxemw sfps krtk umta vnk ewmbx nrlje ymrtqrz mxewb kjxunbt')
puzzle_set.append('egnuti ozat eltl ngueti')
puzzle_set.append('qtcwoxq rmaf qtcwoxq qtcwoxq')
puzzle_set.append('zws gcoa pydruw qsrk lrkybdf ugr wkrxoj nyvf vitwn')
puzzle_set.append('tmr hhd dojid zwrj bhsim righ keqlep flzunou')
puzzle_set.append('lwoquvy acjowxk tqudk oenvioh nyavyl')
puzzle_set.append('rgh dfhgyke iff cpxhuz hui koe iff hui dmukrei')
puzzle_set.append('bjiumig lcbmbgh vleipx sfawua rnf')
puzzle_set.append('gftfh qwb tfdroe xbno qhgofm vqfoe mux')
puzzle_set.append('ljdrr gyfggai iun nju xrucbis mhrcrh fukr obvuqc whlalfe xrucbis nju')
puzzle_set.append('nxjmjr egqwg arllu xqaahri lzc ivt uhsti')
puzzle_set.append('sqiepba rcmts kvesv nvp')
puzzle_set.append('tiksw tiksw rjni gbhvzm ctbq zuqfyvz')
puzzle_set.append('ibsnm kfka aoqigwo sqouih rxz')
puzzle_set.append('jmymq lxio adtmk umyu sxvzquq bporqnb heol fow')
puzzle_set.append('mepa eckq rqviawv dkqoei ifmngpp jiava rtklseu')
puzzle_set.append('yuycd jiufjci yuycd uowg yuycd udq izkicbr csxobh')
puzzle_set.append('nwu tfsjavb rruoxbn oepcov elxf rruoxbn rruoxbn azglwth jcjm ksqiqpv')
puzzle_set.append('dthfwip zqnwa zqnwa zqnwa')
puzzle_set.append('gso wruece ufl crgnlxv vllsm dpyfm wpa ctxko')
puzzle_set.append('wvpze seodz lpq lpq pmtp wsxs ffppx')
puzzle_set.append('yfxquj phvjn rtwieq rtwieq kgxztyu vbjvkc prqqd lyzmdo ojbrt ojbrt qiqjz')
puzzle_set.append('esaezr rpggiy jey kbzrhu uthus osr xxaiijd qfxlf auhzbx gkigoqw')
puzzle_set.append('yfhcj uvgck cds gjhhrg cmempgj yfhcj cjb')
puzzle_set.append('yxi voxvtuw unwg jqqm')
puzzle_set.append('igvjr ljz rus sru gbjtjt qfeg ztu zjl')
puzzle_set.append('leof ocxns hbkoysh hbkoysh leof')
puzzle_set.append('hab lyxmf yhh qeks fwhfxki xmbcak okqjii nfgzyg bhtfgdj lpmjn')
puzzle_set.append('mgognh tad herere lvwnzx ixwqs zphmuuc etdjz kczsf')
puzzle_set.append('mtej rlolsnn zbl uykek dpkan gmz etxtgj')
puzzle_set.append('mihuieo emjgbp jgks mihuieo iexrfw mjdnr bvp mcuzea xkbusvi')
puzzle_set.append('jvqpj bwt jvqpj bwt gxr')
puzzle_set.append('qpnd fpt tpor bibbpcg hmvguez wqc afl ckviua gpi')
puzzle_set.append('dntmcg jglm sxtnu sxtnu sxtnu')
puzzle_set.append('fzkbptw cbfwo ozvwov wbv gcdd izqo ovwzov lolewo xikqpw')
puzzle_set.append('nkxyxzd kpn datf fki werq mwidqx oiibor zizcjph')
puzzle_set.append('xvgyxym zor ijoy lvwsf fjuara idvvq rreit mqyyy ctio tzwqqhj rnpee')
puzzle_set.append('maqkfpk maqkfpk xukg sfdmnlg xjopvr xjopvr irf')
puzzle_set.append('liujcd vnlkouy dxkwc gto vhjvtw')
puzzle_set.append('swhqhj cas aupsd swhqhj cas bvbooii jquck dtdm')
puzzle_set.append('igh iqicicf ghi pcxt srcrjx gmf gyscphv')
puzzle_set.append('drplj drplj wopgpnk wytag wopgpnk')
puzzle_set.append('zexe ilcqoh qiefb txkuv lirfzv')
puzzle_set.append('ovvpn ovvpn uqeurqx uwzn hgmucj ovvpn sjxulms')
puzzle_set.append('rox silka irhsvym kutus otasof tdneav pcagds')
puzzle_set.append('mkja omu tyshbfq onp trxs lxa tftbv bnpl djhnc zdqfs muo')
puzzle_set.append('tjj rmmqas cbbkxs qio pikk ykyew gxlxt nhsyl ykyew')
puzzle_set.append('frcprg njrz oaxcmhc qben pedm ecvtga nzxwpb ior gaklot dpem')
puzzle_set.append('zyt kncau spoe qlchg sqys wkpbng yflju qlchg vkve bzadbpa')
puzzle_set.append('qtq pkaicl qtq mfkfqvr dnleiq brrjxsx uoyxh pkaicl yvmlug')
puzzle_set.append('firwy imtlp ywl qfa dqrbazz ztzb pcsbwhn zesmlag')
puzzle_set.append('ivey ivey mtvc mtvc')
puzzle_set.append('lhize acwf moa cdeoazd voktshy qmvqq jvmuvk ljfmq tsanygc')
puzzle_set.append('xreiqkc aawrovl pofcsg xreiqkc xreiqkc')
puzzle_set.append('cjbzvn ozds iniqu sdoz gqmki bablvll krs vjzcbn')
puzzle_set.append('izsod htkeqz entxn qtns prpcwu omfnmoy')
puzzle_set.append('kwfb tctzda aztctd tadtcz gyt wunbcub ydiwdin xxk')
puzzle_set.append('epnl ijcp giq ltfk zjcabve zfksmz epnl giq xxxbsom')
puzzle_set.append('ulyukpa mdjsbn dydko uhkdt qms aaaj hustlwu')
puzzle_set.append('zlsbu ohx jcwovf egf zlvpqgx qhejm wrywdmw')
puzzle_set.append('uhxqrzr mmu kjxcalj unuohiq rri yzngnb ikvlxry mfiym qbksdx')
puzzle_set.append('khqciz som yklmm jceb khqciz jspy jceb')
puzzle_set.append('ncwggv njvi nqox krtsn lnm')
puzzle_set.append('bgtqme xaxcoq qbtgme obqual vorfk baoqul lgrb')
puzzle_set.append('jli tsbb nlxjc pkwzmz dlxrj hmho gzguko ilj iyaasm')
puzzle_set.append('wlmw grkumg dynwtyo emxhhqr huluk slpqu uhqcmd absmr ufirmwr')
puzzle_set.append('pbs pcammxv dplfr tzvmav nccyy blvyq ffhnz bccutq')
puzzle_set.append('hgge ghge vxmvz hqxgjdg zab guo gheg')
puzzle_set.append('ylj bucoyoq udndc wpgyrbx ueh udndc gxdsdh hdoz wwgqlg')
puzzle_set.append('cjdeh gttyqe kdkm ltzd lfeozse quvjq mnwhokm kdv oojxm nxt')
puzzle_set.append('mfkzus knqxt saxkqww njx zumsfk sbmcyad cpt agvbuv')
puzzle_set.append('tukn vyco yobvsn bzgnn klrnzy kea thzk pxpwq ryfff nxzm')
puzzle_set.append('ylbm lxlz lybm lzxl')
puzzle_set.append('wgtxoij zad slgsi cvnxfg iomswwl vmx')
puzzle_set.append('hkm yinhnkj kmh kwkw kayknck chur styjif yknakck')
puzzle_set.append('rtfwhkq rtfwhkq zsf zsf')
puzzle_set.append('sldq zlntr ueegiw kajivqc ozcbm ceft snvugom pdyc elppeed nnqrp prwwf')
puzzle_set.append('lhk xjonc muc tudag tsafx mmivb dvrjbp qgrew')
puzzle_set.append('hnzer fbgqp aazta aazta lxaz lmgv aazta')
puzzle_set.append('victgxu victgxu mlpd ummrnbx cazjgnw isxcyp efy zfa cyusj')
puzzle_set.append('gyojxo onzq gyojxo uxufp awi ilhl wefwfxr gcjlt tmliynw uxufp pdcnxah')
puzzle_set.append('wjwachn xkuhfbp oky oky ybaeqkr rbuix yreoaw wepmye brvon aasb')
puzzle_set.append('kiidorw vxtxiqx wtqvbrv efdth isel qbom vcssyc vxtxiqx wtqvbrv riafzsw mqzsj')
puzzle_set.append('eurpjd vkhdamt tmfx czeoot hiz ykz lmixzq tfur jhzr')
puzzle_set.append('ipuftpj qbll sqkkdw fwncmiv bri oeeh lehd ioh wag')
puzzle_set.append('suima nanngc imrmc krq atxdo woy atxdo akev qlr aezco qlr')
puzzle_set.append('cfc efwbzck ozkmcxv moczkvx ccf')
puzzle_set.append('bnekky iakrk sask uwgnjp iyi rynev bdnas ldh kass')
puzzle_set.append('sicmw vvjbvv cap nsumc xgvrlm wsoo uoqdu psykckm')
puzzle_set.append('ugg mtr wnzhmmh tjxc ehwnji lwhu mdsckk yvmk enubrqo')
puzzle_set.append('grb oxmxz ohu ytetedv ssx apzlppg fdkamm sxofc jdt ynmu wyejok')
puzzle_set.append('umoep rbyqm eqfk twqnog cptbbi dragna ngqs ffb cexxnc rbyqm')
puzzle_set.append('utizi ormkel wvwur bdx ecelqbv xiccama aag glfvmj')
puzzle_set.append('znb rsuqoa uxo svc')
puzzle_set.append('obs lbifa cffi catpd')
puzzle_set.append('qkxwian ajlzjz wewduzp bbyv qmt fsr qgiu epinp ghmf')
puzzle_set.append('hatg bfgmb aght ghat')
puzzle_set.append('kuq inp dun cknbun wmwsu drlmmg kyxc bdl')
puzzle_set.append('bddybth swdbf jhi fva qpobio bjwm wjaztp jywi')
puzzle_set.append('mgckz vhveu zkemhp zdf xtiqqew mlx wazgd')
puzzle_set.append('umbjq pya lvvxf jeavij rhrxvew bwjqgpr piz')
puzzle_set.append('xaycpwo vjcuc qksc yuixhni sfbfb dydyaq gdfvb tggg xidphvf bpjdrl goskxym')
puzzle_set.append('agxfoip gguif wvo agxfoip ntkbaw fbyggy ooft zxih')
puzzle_set.append('nzvsu ffwq uxvfbl qrql olhmhom qhdltg ymwz krtndtx olhmhom nfsv krtndtx')
puzzle_set.append('qdp jqk ustz xjripzv mnk grnodk pjwdsj uug zqxjqj')
puzzle_set.append('mufrcox zunisfs ocvcge acamm xua vor bsde kxr vor kxr orccxx')
puzzle_set.append('ncycbp anvcxay bmm wndmeaw oso knmk mmb wamenwd kmkv ppdd')
puzzle_set.append('motdcn xzagzwu vuzt utffrn yuqxzrh uvzt ujttq')
puzzle_set.append('tauoqy coiy ybesz tauoqy wpmr trquyne ahxbj jzhems dsdy')
puzzle_set.append('aczq ypw pgmzz srfn quatjgf')
puzzle_set.append('cih ypapk bfxvr euvhkk gugru auhqui')
puzzle_set.append('vyf pssgfvy dnhvbfl xpacme dnhvbfl mzdv iynq hcqu')
puzzle_set.append('lbzvbu hhxiq hdfyiiz iyzihfd xhqih uzdqyxr')
puzzle_set.append('iapbdll vdr cprmrkk vdr dfjqse mlry flpqk vdr')
puzzle_set.append('grrfkq xcpxd grrfkq dxc bjpr prvwh swoc swoc')
puzzle_set.append('bopo chvwuhf qhd ieesl xey ieesl fnjcbe')
puzzle_set.append('kic fyq hsucnu agwyl pzzmd hqksh psw')
puzzle_set.append('mxf uau iti lcoz lpg zbu ocre wqlocmh mxf nidqj lcoz')
puzzle_set.append('bypmix ptzxgmf xmtzgpf hrvzzq')
puzzle_set.append('lbfw zwusma lbfw tuyyy')
puzzle_set.append('lrf uej unswvh obgsb npbl zajr kenea uej qnyjcu wzufim qpzkgya')
puzzle_set.append('qcrxj llyu kligt hlm ehwtbx dda lgsvhdt xewfcv uikn')
puzzle_set.append('nfzjx izqdbq mfbxs imiuc yqxb xlmvix izqdbq eflqfq wku omgtuu izqdbq')
puzzle_set.append('lasdwg hiy btzt eefd eyoep icn nnmhg otml rek luixac nyzgn')
puzzle_set.append('vekteds utsuxdx utsuxdx vekteds')
puzzle_set.append('feyov qrij zbebwg ijrq seplram wttkwm zewbgb kzuhuh')
puzzle_set.append('dmkgtv wohgqo ddtqmv zatahx mym hqowog tkmvdg')
puzzle_set.append('vhha wjrmuyx kqh vyyrj xzchbi ejsdq orlxg vyyrj dlrc')
puzzle_set.append('yetngqn zdtuqox hkarjei fqpsgh eaqwbg zsssog ghb gddqqzr hbg')
puzzle_set.append('obldb zsrhz zxp uxphnev mwnbc pfjft fms xwslk vjm fxy')
puzzle_set.append('nfij dbfykv ttq gyjgac igxuyqi gtiioqx ilhdex dbfykv uyp bdiwya gqf')
puzzle_set.append('pffzruz vogfosh dcs wje')
puzzle_set.append('pohhf fhpoh oon yyz')
puzzle_set.append('xxuam afwm qxl lnt syyr bwxhhf sozauq shlhfmz kwnn milav ochq')
puzzle_set.append('wefcqrt gejw cwerqtf fttf gjew')
puzzle_set.append('jfsvnmr osca epwtle pgfif sxom')
puzzle_set.append('exlfzmq nakp rgdnx rrcvth vhrrct aajjdrt ryyg dsozd jdqlqj pakn iruv')
puzzle_set.append('rmcvo txszcs xxhyxz hbsozk wshkocf rmcvo rcbnt')
puzzle_set.append('kitz yjgney yvkymef nauj hmllsgl kyhm kqr pzsu rcf pzsu qpte')
puzzle_set.append('cdinpx bfur mkj naz ihkheyr nohhoe')
puzzle_set.append('ylris xeqcgup wap bbfih tgfoj')
puzzle_set.append('ina gnlnm zyeqhij cudfuf ipufae bvkdzni aat teqsg cudfuf bjokrbl teqsg')
puzzle_set.append('aedx edax dnfwq qndwf')
puzzle_set.append('rdngdy jde wvgkhto bdvngf mdup eskuvg ezli opibo mppoc mdup zrasc')
puzzle_set.append('qcnc iaw grjfsxe gnf gnf')
puzzle_set.append('zbjm snznt zelswrk gkhlnx dqxqn qqxnd dmro')
puzzle_set.append('zisecvx ztezof uzbq otnrtj qsjzkwm ewvcp rlir bfghlq tgapdr qxmr')
puzzle_set.append('ipnqj opjf vabyoe wkwnd')
puzzle_set.append('wyf mfqxnrf apm snarf jqu aaghx pwecbv lvghayg')
puzzle_set.append('acncv jmmbwlg oiphlm ifuo cvt')
puzzle_set.append('pvmb egansnd zmh gcuzzci rrxpslv ubith')
puzzle_set.append('uoleptg xbouzn xbmg cfh cpn wpqi xbouzn xtxis sxzpns')
puzzle_set.append('rilybri kurbpq vfmjpck tjyogho hfyxad svfofx lfbbhxj khaerfs iqr')
puzzle_set.append('seaebgz wlmtkre qguv qguv wlmtkre')
puzzle_set.append('sgo edkxya zdqgwtt gxu nibuu rairqoq mzxli dci qsv')
puzzle_set.append('tsol mdhzqr rmaqnru ggvcq arbwkn hlkcnj ljkcuof')
puzzle_set.append('mmliphp ocup puoc eijjv')
puzzle_set.append('gmajqpb ijki ijki kvz')
puzzle_set.append('pmqss unhlpcj dlkll nuhlcjp expe tlurzmv nsy vlumtzr tgseozl')
puzzle_set.append('gkvaoni hsba hsba viuedv phyoclp fdq phyoclp febld nqfs')
puzzle_set.append('rxvdtw abn pntv qrqfzz slsvv abn lrxix mnu npot')
puzzle_set.append('ghlfjp woy xwkbmv bkahpkj jve cncvk jvdype fwgvoju yrkwjp gwfvln mvkv')
puzzle_set.append('kmluh mie bby fwer chsinb ojglqr nqk mie')
puzzle_set.append('yzmiu igkgca ybnsqja jpfejtp yjddy xsosxfi ingx qwuhb emrkwpx idqjmmm')
puzzle_set.append('btrllw mphm dkvo ewdl dchcul yah btrllw kmqi mtvgk wtb')
puzzle_set.append('hxsgard yuikc lykt tdee adprp gpougod klnzk mzsmlb')
puzzle_set.append('hdn znblw ifoblur bwzln dbv')
puzzle_set.append('smofpbs vjuyiro llk lfzesga tybu tybu')
puzzle_set.append('gffnpug xaup iqiyz fjkpnkz drrk fwyxw lwzfskz gslwpmv vjxylva tbkyo nib')
puzzle_set.append('evydmb nhwuiiu fkerq nkgbuyy uclrs ydjgglh xhotwbm riirgzt')
puzzle_set.append('bsub eavbt uvd dpzwyt rhn khrbptt xszckc djnfxju axofhat powmso nvdffrv')
puzzle_set.append('xtuykl fjz mbikc xpnx hmey fjz fjz')
puzzle_set.append('rkls nwdcsyx rkls rkls')
puzzle_set.append('tygml untequ ybdfumz nqffbq uipc sove hfnqj')
puzzle_set.append('ytecew vven koqn royynd qsn ksl qsn sdw')
puzzle_set.append('hknlw qwho whoq oqwh')
puzzle_set.append('lzmmtqu qvhyeo cnofuj utpwkjz gnirz yhhu aodbnd')
puzzle_set.append('zsr axw kwtzcv tydzo kwtzcv lkxsm')
puzzle_set.append('rbjtqe nihifd gvdxd bpxzy rxteky vgcgllv vbbua anygiup rqo')
puzzle_set.append('dpd wblfwp wblfwp wblfwp ygahc tqjbaq')
puzzle_set.append('gsw gsw pacgj xmrcz zmxhmch xmrcz')
puzzle_set.append('pdq rhe xqmq lgpkhg fyffrot ovnqh wle')
puzzle_set.append('tbjavke ypzzrj jizx gdxoh icjsat otfh fmygumv')
puzzle_set.append('snch nxlgjgp jeyn sxoqfj jtage jtage iuice')
puzzle_set.append('rtb coefuj grwg grwg rtb krhqnma vfhgbr')
puzzle_set.append('vhegtl btorwxg szcev kbvkx itsk nlzpbed')
puzzle_set.append('hiukrf ilzkm yllhh xsgwkdp zyy kjbv')
puzzle_set.append('rfcg tdorci zcj wzftlv rfcg rfcg')
puzzle_set.append('lgbc lzizat vsno pau nvv vsno bbr lzizat qhtb gwp')
puzzle_set.append('sfwnio tcugjk bsfsz ykyfwg ibkap fsrvy mygk kzunawx zyhyh')
puzzle_set.append('mpavlh qps bylh lttjkz rqabgk vewb bwev tlzkjt gzrbxga ktmso prpkj')
puzzle_set.append('gpf ims ynh ffrs vpa iemp gofh cgbauje')
puzzle_set.append('secys qks mcnfhwh drog kqs pajy zoltkw lfihnb myb ioxptu')
puzzle_set.append('ytq nrta ouk ajqblf yuwwcd zdy blyoxbw dakk nvgi bzrhzaa')
puzzle_set.append('nkoych sufiia xkdvw crtldee zycl qblab egqhr qblab')
puzzle_set.append('nllno muxaf vds qjnitmw zkpj wskyhft kmqct xamuzpw qcai cdjtbt kaxv')
puzzle_set.append('qzdytpe osr fuw osr qzdytpe whperd rydwdcl knoa')
puzzle_set.append('zkdznhd peh duoygr zamrgl irnvj otpe pltpq jdkecg')
puzzle_set.append('byzgw rece iigdug ehif tpgje')
puzzle_set.append('ccnn foqdran gbctca tefdjxh ntcr rjciii xip xlss crl wvvhzqm twyohf')
puzzle_set.append('dqyii milqqc qjgkojp qjgkojp ryde')
puzzle_set.append('tdkyj tbrcud tsba vqtmb cjwxnf')
puzzle_set.append('hqhmq wemvrce nagig pwnw nagig epg nagig vlsi')
puzzle_set.append('tqgvw luoplw hccti npjm rytdruq cylrsun rytdruq vjsbjl rytdruq ppti')
puzzle_set.append('itgt tuwc itgt rvp itgt tigns eipl ksmru')
puzzle_set.append('pdw wdhtkn nbdbpn wff zhuuipg rvemv qxr')
puzzle_set.append('qgkwdq cjilayh ymeks mrpuzai dwgs stfstgz ucvqhb yout oiq')
puzzle_set.append('vpxik ypfr qytimvu qms oxbmw ppyfx')
puzzle_set.append('fwwidn gdhd pyuexk snsz iwndfw')
puzzle_set.append('lfcb sllxjna lfcb hpzahfg mmvgaa svny jhuzd')
puzzle_set.append('unyg gicmzd fwc spkciy toyq wjupckd vzzx iuqgka ytqycb pxsufj')
puzzle_set.append('goj tnrcml eyizngj txa xrkiw zvu igduz')
puzzle_set.append('wek xrrlkna clyof rrlnxak')
puzzle_set.append('cjm rmyuku vjom gtf')
puzzle_set.append('buk cfae awstd dywgqp hxo wcxvf laihqw xdqfes wdbh qceh uzlwj')
puzzle_set.append('sudguo dxwplto rlebdh bkamu dxwplto')
puzzle_set.append('crwkyxm yuz kjtdhom crwkyxm')
puzzle_set.append('trhc sduorxr aizfryh rsudxor gbyc')
puzzle_set.append('pczkyl bptp qnn nxmpwsx udrg hhlb rubtrmx twzodlp xygnht')
puzzle_set.append('jmqct cden yfajtkz fevcw sxonbxz sxonbxz qkzkm hhngr fbv')
puzzle_set.append('sdsnm mwvicr wypfi cty ndbowr woiz mrauwzd qlno mwvicr')
puzzle_set.append('vteyo fng lvr lxytn txpj milg')
puzzle_set.append('wjx ahtmgo cgwcaj kaxae fhlvlqf')
puzzle_set.append('ezj eetqhzu upwda iiefwlk vyvby')
puzzle_set.append('imalvy yeghqe jwcu mvrod cwju')
puzzle_set.append('bxnmsa yhfu npsdar tsbri hfuy sirbt oofxmy')
puzzle_set.append('fkndt elbjtn vepqtxt elvpf fpelv bzkgag qttexpv prblwb')
puzzle_set.append('rmq iqs yvprnyy iezqrzm wlqsrr')
puzzle_set.append('yviovq lekxghj oey qwhzj lxknxw qiyovv ksnt jptz')
puzzle_set.append('tyrg cifxt hugqf tyrg ffuiv jmax qyw fozfosq ffuiv')
puzzle_set.append('nmg rsl jpzazd qbtlf yxqtsj czwmdfd bamge lbjdof uqy jssc')
puzzle_set.append('cbx boozjip pwgvzlq rjz kxy kxy hszacok fvsq jhnir cnsba gafz')
puzzle_set.append('sbcuxb wfur nnnfqjj fdwg huhe sbcuxb')
puzzle_set.append('icwk qelbxs uevp qped zsnhh wpuok wddxsln ftnzupr ruxol cgxjb jbhh')
puzzle_set.append('izcp htykj xxmndoq amnspe htykj')
puzzle_set.append('vverol oixwlny vqd tvfzu henc gnyrwr')
puzzle_set.append('ytxio etytsx choynep zqapo hfjit')
puzzle_set.append('lkvgr oyzfa taiqr jok djatvy ckif tmdw oyzfa zroy')
puzzle_set.append('jlgpyp kkqysg oqjki hjohoug hbhta muilz zft')
puzzle_set.append('sumfyu wftcu bwwdcy lezimwa qwvxv zwh mqyv bmfot aii torcol rnt')
puzzle_set.append('tpdj xrw ccsbnh fhptv fwkxjfm dmqaokd bjci')
puzzle_set.append('zxi vmf vmf dpyg')
puzzle_set.append('sfzxysw lcms bkojtv bkojtv')
puzzle_set.append('opywo qll ipkitr mtwp tudrr svhyp huz bxsdpn xomfy')
puzzle_set.append('gkod luo qrosbp orbd rpsjzyd rlh gdok tze')
puzzle_set.append('nusiuq nusiuq zeys ahufexc')
puzzle_set.append('veno jntg avtmtdn qojxru zegdcql odfcetz pgehau')
puzzle_set.append('uqun vigjm ykac ozlelj danmji bibugox')
puzzle_set.append('rpuozh ajwru rbvuevv uhzsq')
puzzle_set.append('iawoe tyb aewio ymf byt inijv ctu fcys micsgzl pbby alt')
puzzle_set.append('gktyxp ris mqpfm bkqsfl nrg idbbcxg jhcf')
puzzle_set.append('qibt invvv qibt luitx rnm eby hrfbmwl wnap sgkzvb qlwc hrfbmwl')
puzzle_set.append('jwkv qecsjbw lycgldd wjvk tjcp dycldgl pzrvr zrlcf kji')
puzzle_set.append('nzsrmiq nmhse ilivrk kqv')
puzzle_set.append('besmyzi imkgpt iekbjax abxeijk uvzs wwv')
puzzle_set.append('jdocl uki ltswp tjkljc ymce iuepze qygqxzs tei lkry')
puzzle_set.append('hhyfy gvzd mqksxlq czn afe mesnag eep frwgekg mqksxlq phpy')
puzzle_set.append('ehg connnza ekt ddgokw')
puzzle_set.append('mpbsoms uzhzl xevww ztt uzhzl')
puzzle_set.append('lftybr firc awsud dsxdkk ltf ipjv dtx lcymth')
puzzle_set.append('vkcpb gxtxq yioeq fexj xxgqt')
puzzle_set.append('srvca fslnnvf nfmkpvt egw wemumq jie vznf dzsjw cukf kcvyir')
puzzle_set.append('yxjkl lyjkx jyxlk kgc xtz')
puzzle_set.append('tpoe xzov csp leleoqo noyre tdhf cyib sjgtdx raehdw nmcxp')
puzzle_set.append('qvt uhznqe bpvos vtq ddlebtd tqv')
puzzle_set.append('xlw utsxs gpia rvlvnts elkxr dddihy tnrslvv ibf wlx bxg')
puzzle_set.append('cwqnnrt rkkqyf dye yde fzl pthanj')
puzzle_set.append('boc rqjenpp xjqte jteqx pvoofc pidqe ruoucy gvnro ognrv')
puzzle_set.append('qhalb gnazwc fhl iuti')
puzzle_set.append('clnbjfo nnfs nnfs heymvr oarew oarew nxu')
puzzle_set.append('lwtrotg hiaxwj ymzbly nvhzjhj zlsaheg nvhzjhj ymzbly')
puzzle_set.append('rrvi tsjp tsjp tsjp killji')
puzzle_set.append('rpx hiclj cmwq ibhj nfd')
puzzle_set.append('pvwymn iebkd xmpw vuhhkap ksw zigzy mzzyyxy rmuh iwwhea cglfq')
puzzle_set.append('rlwelgy sffml jin qsdzro xlsty mgqzuu etxjuo emzd jgnoyq tkjuy vfvb')
puzzle_set.append('tkctdj hhkuc viskmy obw')
puzzle_set.append('zvjkuj akeky ikj jqd hfhzbwe bkc')
puzzle_set.append('btev nrdo hcyiuph stf qharfg vpmel mpfz nvs ytgbbc')
puzzle_set.append('ieepn ndueuw svmdr tcvumw mceyrn mrjwhyl tbdj mgrgvz')
puzzle_set.append('uxrs ckyi xpmqm czzrkl cjp')
puzzle_set.append('nlliwd wrqkrkz yjmng nlliwd zirde hcjjn wco ysf mgl')
puzzle_set.append('dxti lcahe ommare izlwf ramsfb nzgfvo ijvm fwymrdu bndq')
puzzle_set.append('isxy jpvuzu tdduyhw dixp cfa fkzbteg ytoi kepk ysf yqcpi')
puzzle_set.append('qmeprfj soqo ncgeor cqsuuj grzy wogxy vyblnbg slvtry vdols kka')
puzzle_set.append('ltykfp gtzl olrp gxend vapee deq')
puzzle_set.append('emywfbn dbfiut rkt wvwe dbfiut bwffhea yuzcxv gogpicp wvwe')
puzzle_set.append('vqvmrp ofbk dlfabd jwllzxk obx vqpwjj umvng tqwis fstxy fstxy')
puzzle_set.append('miha zgvyux rmraszo xwf')
puzzle_set.append('kjaagk btm kjaagk wkewjrg kjaagk')
puzzle_set.append('lbmli aizs omrdr gzktnx asiz ptanzpa xlo ljre ckyb wob')
puzzle_set.append('svz dlk rijagg avxmg fkzwhk uro gegm')
puzzle_set.append('dzplum temdw jqnm tvxcww bmg tftttpp deuw comxey xfimzjx caluczi nqn')
puzzle_set.append('uwvhxa ztkd nlsdyt vihl julkwwv uzch dwakhs')
puzzle_set.append('wkhuihh ycrc cxff vzcfhpp uegfd gaok kcnvz lhzogq lwa tyrypvu')
puzzle_set.append('idp zmrrzp zmrrzp nktp xsnx rjsxn')
puzzle_set.append('eybrnib ivgntl vaxsbpi eybrnib')
puzzle_set.append('nzvnq xvbfa pbhwwh ylju runvsj imlx vztesn')
puzzle_set.append('nfdohd nfdohd gtevnky pivjyct ihvd fzcsrq lko fmqk')
puzzle_set.append('kwpkks ecikxu bcxswlt qvrxm sbcqmh')
puzzle_set.append('kdjrmj piuh kdjrmj vnaf gyedkg vptxgm xezssxx zsg qjzpo zsg')
puzzle_set.append('oqo sley aqx qmpqb fgmylbj egd zivj kepxizv kuakyn lunbnd')
puzzle_set.append('hmcf hmcf xlhgc hmcf cdlm buofnx')
puzzle_set.append('onjcj yluonz kzmk phqo phqo phqo')
puzzle_set.append('ohaafy efl bnkkjww wwjnyoj dxeaig ywnjjwo slk hrbebw ohlyju elf')
puzzle_set.append('msohiqz aunk njki bfktdgi htmyrj mgx')
puzzle_set.append('numlzrl rmnlulz glb ltt fhbajz gqxpu')
puzzle_set.append('gko hco oai ryq xwy sdqosft spjkiu cxfhg ycwpglh noy rah')
puzzle_set.append('btzpjem brpk vqr atxu rhlh rqv jmg fvyus')
puzzle_set.append('phmxxgj ejx xje qtk hsb kqt npwj gqt')
puzzle_set.append('hujyjp nwmsd ant zipuya lrkahww uwqal vzlo qmbo twkjkse ufivi')
puzzle_set.append('zfbnyz fwvh xrnrw usn zin daq iwjzj')
puzzle_set.append('yykyg iwypfy hehqnl cjvk cevdrec')
puzzle_set.append('gui muuto wsta glqmx gfo rdmbv mxwz gffzt eejpw gion')
puzzle_set.append('lpng nduid iqbpu nduid knrqd')
puzzle_set.append('xwxn oefpckv gjaua ugaaj gjuaa')
puzzle_set.append('qxk aeql trqdmqc crzlinj crzlinj trqdmqc rijcne ewyf')
puzzle_set.append('rfv qmbe fvr bmeq')
puzzle_set.append('upqyfw lowzq wpen upqyfw gfskbil sljuzh wpen')
puzzle_set.append('bdcara qyhx rtaez qyq gbyr')
puzzle_set.append('evzls qxtxq clzd svbgqi zxlzgss vtrre fko eebo qjyl')
puzzle_set.append('zaapeo kpwhz tygknau nyd pch trp xqe')
puzzle_set.append('ypzcafg rnqmbh qtteg sncu ssojhhm zonfym thir xmgheb wqj gpjg ssojhhm')
puzzle_set.append('wvcwyn xrf muozyya lasdp xpjgu kpqv zkiihiv ifje cbdlavg xbied hfnaa')
puzzle_set.append('qqqb rettz rycukl ihpkhh')
puzzle_set.append('dnxzxqv znb znb fbxj azxtezb xvxa')
puzzle_set.append('peqkd xlzqkov esgnw ucku hrwpfxd xtd vnig vlmfp ajte qswr kqoj')
puzzle_set.append('dpwy oavzkk dwyp ehij upqxgii pydw')
puzzle_set.append('amfc hfv xmqa nqvn cal rqmcq oej amqx cla ntxj')
puzzle_set.append('hqhhe qkbhwli wmhlcq xaczs peywuo')
puzzle_set.append('vcr xfv xfv kymo qpszwzo xfv')
puzzle_set.append('nmrbur tswo xbo ljlrzo bmhpgc pev zovkznz lok wbbhtkk')
puzzle_set.append('tojj lxqgr rhjavrm ndsdup gdbjwaq cqpnl wfaxivl rfry ryfr udspnd')
puzzle_set.append('beffod sknlph amb feobdf')
puzzle_set.append('mldgn jxovw yuawcvz kzgzwht rxqhzev fsdnvu vluuo eycoh cugf qjugo')
puzzle_set.append('tlnd qcxj ker fdir cgkpo nrqhyq raef uqadf iahy rxx')
puzzle_set.append('mhvisju lhmdbs tcxied xeidtc ujry cditex gvqpqm')
puzzle_set.append('cgc jazrp crgnna uvuokl uvuokl uoiwl sknmc sknmc')
puzzle_set.append('rvbu czwpdit vmlihg spz lfaxxev zslfuto oog dvoksub')
c = 0
d = len(puzzle_set)
for i in puzzle_set:
    if no_duplicates(i):
        c += 1

print "{} of {}".format(c,d)

# 175 out of 512 - wrong, too low!

# doh - how many are VALID, not INVALID, is the question:

# 337 of 512 - correct

# part 2: 231 of 512 - correct