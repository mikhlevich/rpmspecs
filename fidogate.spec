Name:           fidogate
Version:        5.2.4
Release:        1%{?dist}
Summary:        Fido-Internet Gateway and Tosser

License:        GPLv2
URL:            https://github.com/ykaliuta/fidogate
Provides:	binkd
Source:         %{name}-master.zip

BuildRequires:  libtool
BuildRequires:  libtool-ltdl
BuildRequires:  autogen
BuildRequires:  automake
BuildRequires:  unzip
BuildRequires:  glibc-devel
BuildRequires:  gcc-c++
BuildRequires:  byacc
BuildRequires:  inn
Requires:       libtool-ltdl
Requires:       bzip2
Requires:       unzip
Requires:       zip
Requires:       bison
Requires:       inn
Requires:	postfix
Requires:	binkd

%description
DS fork of fidogate. It can be used as:
 * Fido-Internet Gateway
 * Fido FTN-FTN Gateway
 * Fido Mail Processor
 * Fido File Processor
 * Fido Areafix/Filefix


%prep
%setup -q -n %{name}-master

%build
libtoolize
./autogen.sh

%configure --prefix=%{_prefix} \
	   --exec-prefix=%{_prefix} \
	   --with-logdir=/var/log/fidogate \
	   --with-vardir=/var/lib/fidogate \
	   --with-spooldir=/var/spool/fidogate \
	   --with-lockdir=/var/lock/fidogate \
	   --with-btbasedir=/var/spool/fidogate/bt \
	   --with-sysconfdir=%{_sysconfdir}/fidogate \
	   --with-newsbindir=/usr/libexec/news \
	   --with-rnews=/usr/libexec/news/rnews \
	   --disable-desc-dir \
	   --with-owner=news \
	   --with-group=news

%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install prefix=%{_prefix}/.. exec_prefix=%{_prefix} libdir=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc TODO TODO.rus ChangeLog Changes.ru doc/README doc/FAQ.ru doc/README.ru
%license COPYING

%{_bindir}/areasbbssync
%{_bindir}/areassucksync
%{_bindir}/ftnaf
%{_bindir}/ftnafutil
%{_bindir}/ftnexpire
%{_bindir}/ftnfattach
%{_bindir}/ftnhatch
%{_bindir}/ftnoutpkt
%{_bindir}/hosts2dns
%{_bindir}/logcheck
%{_bindir}/logdaily
%{_bindir}/logreport
%{_bindir}/logsendmail
%{_bindir}/logstat
%{_bindir}/ngoper
%{_bindir}/nl-autoupd
%{_bindir}/nl-del
%{_bindir}/nl-diff
%{_bindir}/out-attach
%{_bindir}/out-freq
%{_bindir}/out-ls
%{_bindir}/out-manip
%{_bindir}/out-rm0
%{_bindir}/out-rmbsy
%{_bindir}/outb
%{_bindir}/outb-kill
%{_bindir}/pktdebug
%{_bindir}/pktmore
%{_bindir}/pkttmpl
%{_bindir}/recvuu
%{_bindir}/runchklock
%{_bindir}/runinc
%{_bindir}/senduu
%{_bindir}/senduumail
%{_bindir}/sumcrc
%config %{_sysconfdir}/fidogate/acl.sample
%config %{_sysconfdir}/fidogate/aliases.sample
%config %{_sysconfdir}/fidogate/areafix.help.rus
%config %{_sysconfdir}/fidogate/areafix.help.sample
%config %{_sysconfdir}/fidogate/bounce.acl
%config %{_sysconfdir}/fidogate/bounce.acl_netmail
%config %{_sysconfdir}/fidogate/bounce.addrinto
%config %{_sysconfdir}/fidogate/bounce.down
%config %{_sysconfdir}/fidogate/bounce.insecure
%config %{_sysconfdir}/fidogate/bounce.noto
%config %{_sysconfdir}/fidogate/bounce.restricted
%config %{_sysconfdir}/fidogate/fidogate.conf.sample
%config %{_sysconfdir}/fidogate/fidokill.sample
%config %{_sysconfdir}/fidogate/ftnacl.sample
%config %{_sysconfdir}/fidogate/hosts.sample
%config %{_sysconfdir}/fidogate/packing.sample
%config %{_sysconfdir}/fidogate/passwd.sample
%config %{_sysconfdir}/fidogate/routing.sample
%config %{_sysconfdir}/fidogate/spyes.sample
%config %{_sysconfdir}/fidogate/uplinks.sample
%{_libdir}/libfidogate.a
%{_libdir}/libfidogate.la
%{_libdir}/libfidogate.so
%{_libdir}/libfidogate.so.5
%{_libdir}/libfidogate.so.5.0.0
%{_libexecdir}/charsetc
%{_libexecdir}/confval
%{_libexecdir}/ftn2ftn
%{_libexecdir}/ftn2rfc
%{_libexecdir}/ftnafmail
%{_libexecdir}/ftnafpkt
%{_libexecdir}/ftnflo
%{_libexecdir}/ftnin
%{_libexecdir}/ftninpost
%{_libexecdir}/ftninrecomb
%{_libexecdir}/ftnmail
%{_libexecdir}/ftnpack
%{_libexecdir}/ftnroute
%{_libexecdir}/ftntick
%{_libexecdir}/ftntickpost
%{_libexecdir}/ftntoss
%{_libexecdir}/report_traffic
%{_libexecdir}/rfc2ftn
%{_libexecdir}/send-fidogate
%config %{_localstatedir}/lib/fidogate/areas.sample
%config %{_localstatedir}/lib/fidogate/areas.bbs.sample
%config %{_localstatedir}/lib/fidogate/fareas.bbs.sample

%dir %attr(700,news,news) /etc/fidogate
%dir %attr(700,news,news) /var/log/fidogate
%attr(-,news,news) /usr/bin/*
%attr(-,news,news) /usr/libexec/*
%attr(-,news,news) /usr/lib/*
%dir %attr(700,news,news) /var/lib/fidogate
%dir %attr(700,news,news) /var/lib/fidogate/seq
%attr(700,news,news) /var/lock/fidogate
%attr(700,news,news) /var/spool/fidogate
%attr(770,news,news) /var/spool/fidogate/bt
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/acl.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/aliases.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/areafix.help.rus
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/areafix.help.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/bounce.acl
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/bounce.acl_netmail
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/bounce.addrinto
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/bounce.down
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/bounce.insecure
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/bounce.noto
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/bounce.restricted
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/fidogate.conf.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/fidokill.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/ftnacl.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/hosts.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/packing.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/passwd.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/routing.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/spyes.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate/uplinks.sample
%config(noreplace) %attr(600,news,news) %{_localstatedir}/lib/fidogate/areas.sample
%config(noreplace) %attr(600,news,news) %{_localstatedir}/lib/fidogate/areas.bbs.sample
%config(noreplace) %attr(600,news,news) %{_localstatedir}/lib/fidogate/fareas.bbs.sample

%changelog
