// Copyright (c) 1996-1997 Athenia Associates.
// http://www.webreference.com/js/
// License is granted if and only if this entire
// copyright notice is included. By Tomer Shiran.

function setCookie (name, value, expires, path, domain, secure) {
    var curCookie = name + "=" + escape(value) + (expires ? "; expires=" + expires : "") +
        (path ? "; path=" + path : "") + (domain ? "; domain=" + domain : "") + (secure ? "secure" : "");
    document.cookie = curCookie;
}

function getCookie (name) {
    var prefix = name + '=';
    var c = document.cookie;
    var nullstring = '';
    var cookieStartIndex = c.indexOf(prefix);
    if (cookieStartIndex == -1)
        return nullstring;
    var cookieEndIndex = c.indexOf(";", cookieStartIndex + prefix.length);
    if (cookieEndIndex == -1)
        cookieEndIndex = c.length;
    return unescape(c.substring(cookieStartIndex + prefix.length, cookieEndIndex));
}

function deleteCookie (name, path, domain) {
    if (getCookie(name))
        document.cookie = name + "=" + ((path) ? "; path=" + path : "") +
            ((domain) ? "; domain=" + domain : "") + "; expires=Thu, 01-Jan-70 00:00:01 GMT";
}

function fixDate (date) {
    var base = new Date(0);
    var skew = base.getTime();
    if (skew > 0)
        date.setTime(date.getTime() - skew);
}

function rememberMe (f) {
    var now = new Date();
    fixDate(now);
    now.setTime(now.getTime() + 365 * 24 * 60 * 60 * 1000);
    now = now.toGMTString();
    if (f.author != undefined)
       setCookie('mtcmtauth', f.author.value, now, '/', '', '');
    if (f.email != undefined)
       setCookie('mtcmtmail', f.email.value, now, '/', '', '');
    if (f.url != undefined)
       setCookie('mtcmthome', f.url.value, now, '/', '', '');
}

function forgetMe (f) {
    deleteCookie('mtcmtmail', '/', '');
    deleteCookie('mtcmthome', '/', '');
    deleteCookie('mtcmtauth', '/', '');
    f.email.value = '';
    f.author.value = '';
    f.url.value = '';
}

function hideDocumentElement(id) {
    var el = document.getElementById(id);
    if (el) el.style.display = 'none';
}

function showDocumentElement(id) {
    var el = document.getElementById(id);
    if (el) el.style.display = 'block';
}

var commenter_name;

function individualArchivesOnLoad(commenter_name) {


 // comments are allowed but not required
    if (commenter_name) {
        hideDocumentElement('name-email');
    } else {
        showDocumentElement('name-email');
    }



    if (document.comments_form) {
        if (document.comments_form.email != undefined &&
            (mtcmtmail = getCookie("mtcmtmail")))
            document.comments_form.email.value = mtcmtmail;
        if (document.comments_form.author != undefined &&
            (mtcmtauth = getCookie("mtcmtauth")))
            document.comments_form.author.value = mtcmtauth;
        if (document.comments_form.url != undefined && 
            (mtcmthome = getCookie("mtcmthome")))
            document.comments_form.url.value = mtcmthome;
        if (mtcmtauth || mtcmthome) {
            document.comments_form.bakecookie.checked = true;
        } else {
            document.comments_form.bakecookie.checked = false;
        }
    }
}

function writeTypeKeyGreeting(commenter_name, entry_id) {
    if (commenter_name) {
        document.write('<p>' + commenter_name + 'さん、サイン・インしました。 コメントをどうぞ。 '+
          '(<a href="http://www.football-teishoku.jp/x/mt/mt-comments.cgi?__mode=handle_sign_in&amp;static=1&amp;logout=1&entry_id=' + entry_id + '">サイン・アウト</a>)</p>');
    } else {
        document.write('<p>もし<a href="https://www.typekey.com/t/typekey/?lang=ja" title="TypeKey">TypeKey</a>のアカウントを持っていれば、 '+
          '<a href="https://www.typekey.com/t/typekey/login?&amp;lang=ja&amp;t=gM0ML6hgFna5Bu4z0WOm&amp;v=1.1&amp;_return=http://www.football-teishoku.jp/x/mt/mt-comments.cgi%3f__mode=handle_sign_in%26static=1%26entry_id=' + entry_id + '">サイン・イン</a> '+
          'してコメント可能です。</p>');

    }

}

if ('www.football-teishoku.jp' != 'www.football-teishoku.jp') {
    document.write('<script src="http://www.football-teishoku.jp/x/mt/mt-comments.cgi?__mode=cmtr_name_js"></script>');
} else {
    commenter_name = getCookie('commenter_name');
}

