Summary:	Orb of Zot-retrieval-quest
Summary(pl):	Zdob±d¼ Kulê Zota
Name:		crawl
Version:	400b26
Release:	1
Epoch:		1
License:	Crawl GPL
Group:		Applications/Games
Source0:	ftp://ftp.dungeoncrawl.org/dev/4.0.x/src/dc%{version}-src.tbz2
# Source0-md5:	807810185ff93f06bd4e169067644d8f
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-savedir.patch
BuildRequires:	ncurses-devel
Requires:	applnk >= 1.5.13
Requires:	zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	/var/games/crawl

%description
Crawl is a large and very random game of subterranean exploration in a
fantasy world of magic and frequent violence. Your quest is to travel
into the depths of the Dungeon (which is different each time you play)
and retrieve the Orb of Zot.

Crawl is an RPG of the 'rogue-like' type, one of the descendants of
Rogue. Its graphics are simple but highly informative, designed to be
understood at a glance, and control is exercised largely through
one-keystroke commands.

%description -l pl
Crawl jest du¿± i bardzo losow± gr± podziemnej eksploracji w
fantastycznym ¶wiecie magii i czêstej przemocy. Twoim zadaniem jest
podró¿ w g³±b Lochu (który w ka¿dej grze jest inny) i odzyskanie Kuli
Zota.

Crawl jest gr± RPG typu 'rogue-like', jednym z potomków Rogue. Grafika
jest prosta, ale wysoce informatywna, zaprojektowana by byæ zrozumia³±
od pierwszego spojrzenia. Sterowanie odbywa siê g³ównie jedno
klawiszowymi poleceniami.

%prep
%setup -q -n dc%{version}-src
%patch0 -p1
%patch1 -p1

%build
cd source
%{__make} -f makefile.lnx \
	CFLAGS="-DLINUX %{rpmcflags} -fno-rtti -fno-exceptions" \
	LDFLAGS="%{rpmldflags}" \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man6,%{_datadir},%{_applnkdir}/Games/RPG,%{_pixmapsdir}}

install source/crawl $RPM_BUILD_ROOT%{_bindir}
install docs/crawl.6 $RPM_BUILD_ROOT%{_mandir}/man6

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/RPG
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

:> $RPM_BUILD_ROOT%{_datadir}/scores

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc init.txt licence.txt macro.txt readme.txt docs/buglist.txt
%doc docs/changes.* docs/crawl.txt docs/todo.txt docs/versions.txt
%attr(2755,root,games) %{_bindir}/crawl
%attr(2775,root,games) %dir %{_datadir}
%attr(664,root,games) %config(noreplace) %verify(not md5 size mtime) %{_datadir}/scores
%{_mandir}/man6/*
%{_applnkdir}/Games/RPG/*
%{_pixmapsdir}/*
