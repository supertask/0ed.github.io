<!-- Hide This Script From Non-JavaScript-Enabled Browsers



var filename;



function wo_dramanavi(filename){ //	ドラマナビの解説ウィンドウ
	var newwindow = window.open(filename, "drama_navi_detail", "toolbar=no, location=no, directories=no, status=no, menubar=no, scrollbars=yes, resizable=yes, width=540, height=600");
/*	ディスプレイの中央に展開する
	var sx = 760;
	var sy = 420;
	var x = (screen.width - sx) / 2;
	var y = (screen.height - sy) / 2;
	newwindow.moveTo (x, y);
*/
}

function wo_searchmap(filename){	// クッキー設定用マップウィンドウ
	var newwindow = window.open(filename,"search_cookie_map","toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=no,resizable=no,width=640,height=520");
}

function wo_specialpage(fileName){	// 特集ページのウィンドウ
	var newWindow = window.open(fileName,"openprize","toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,resizable=no,width=800,height=710");
}

function wopen(file){	// ドラマナビの相関図ウィンドウ
	var newWindow = window.open(fileName,"sokanzu","toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=460,height=620");
}

function wo_person(fileName){	// 出演者50音順一覧ウィンドウ
	var newWindow = window.open(fileName,"person_list","toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,resizable=no,width=460,height=620");
}

function wo_company(writeFileName){	// 　	株式会社角川ザテレビジョン
	var newWindow = window.open(writeFileName,"company","toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,resizable=no,width=820,height=720");
}

// Stop Hiding -->
