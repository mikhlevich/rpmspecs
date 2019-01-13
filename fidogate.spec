Name:           fidogate-ds
Version:        5.2.5
Release:        1%{?dist}
Summary:        Fido-Internet Gateway and Tosser

License:        GPLv2
URL:            https://github.com/ykaliuta/fidogate
Source0:        fidogate-5.2.5.zip

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

%description
DS fork of fidogate. It can be used as:
 * Fido-Internet Gateway
 * Fido FTN-FTN Gateway
 * Fido Mail Processor
 * Fido File Processor
 * Fido Areafix/Filefix


%prep
%setup -q -n fidogate-master

%configure --prefix=/usr \
	   --exec-prefix=/usr \
	   --sysconfdir=/etc/fidogate \
	   --with-logdir=/var/log/fido/gate \
	   --with-vardir=/var/lib/fidogate \
	   --with-spooldir=/var/spool/fido/gate \
	   --with-btbasedir=/var/spool/fido/bt \
	   --with-sysconfdir=/etc/fidogate \
	   --with-newsbindir=/usr/libexec/news \
	   --disable-desc-dir \
	   --with-owner=news \
	   --with-group=news

%build
libtoolize
./autogen.sh

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
%config %{_sysconfdir}/acl.sample
%config %{_sysconfdir}/aliases.sample
%config %{_sysconfdir}/bounce.acl
%config %{_sysconfdir}/bounce.acl_netmail
%config %{_sysconfdir}/bounce.addrinto
%config %{_sysconfdir}/bounce.down
%config %{_sysconfdir}/bounce.insecure
%config %{_sysconfdir}/bounce.noto
%config %{_sysconfdir}/bounce.restricted
%config %{_sysconfdir}/fidogate.conf.sample
%config %{_sysconfdir}/fidokill.sample
%config %{_sysconfdir}/ftnacl.sample
%config %{_sysconfdir}/hosts.sample
%config %{_sysconfdir}/packing.sample
%config %{_sysconfdir}/passwd.sample
%config %{_sysconfdir}/routing.sample
%config %{_sysconfdir}/spyes.sample
%config %{_sysconfdir}/uplinks.sample
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
%config %{_localstatedir}/lib/fidogate/areas.bbs.sample
%config %{_localstatedir}/lib/fidogate/fareas.bbs.sample

%dir %attr(700,news,news) /etc/fido/gate
%dir %attr(700,news,news) /var/log/fido/gate
%attr(-,news,news) /usr/bin/*
%attr(-,news,news) /usr/libexec/*
%attr(-,news,news) /usr/lib/*
%dir %attr(700,news,news) /var/lib/fidogate
%dir %attr(700,news,news) /var/lib/fidogate/seq
%attr(700,news,news) /var/lock/fidogate
%attr(700,news,news) /var/spool/fido/gate
%attr(770,news,news) /var/spool/fido/bt
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/acl.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/aliases.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/areas.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidogate.conf.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fidokill.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/ftnacl.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/hosts.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/packing.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/passwd.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/routing.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/spyes.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/areas.bbs.sample
%config(noreplace) %attr(600,news,news) %{_sysconfdir}/fareas.bbs.sample

%changelog
