%define debug_package %{nil}
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
rm -rf %{buildroot}
%make_install prefix=%{_prefix}/.. exec_prefix=%{_prefix} libdir=%{_libdir}

%clean
rm -rf %{buildroot}

%files
%doc TODO TODO.rus ChangeLog Changes.ru doc/README doc/FAQ.ru doc/README.ru
%license COPYING

%attr(-,news,news) %{_bindir}/areasbbssync
%attr(-,news,news) %{_bindir}/areassucksync
%attr(-,news,news) %{_bindir}/ftnaf
%attr(-,news,news) %{_bindir}/ftnafutil
%attr(-,news,news) %{_bindir}/ftnexpire
%attr(-,news,news) %{_bindir}/ftnfattach
%attr(-,news,news) %{_bindir}/ftnhatch
%attr(-,news,news) %{_bindir}/ftnoutpkt
%attr(-,news,news) %{_bindir}/hosts2dns
%attr(-,news,news) %{_bindir}/logcheck
%attr(-,news,news) %{_bindir}/logdaily
%attr(-,news,news) %{_bindir}/logreport
%attr(-,news,news) %{_bindir}/logsendmail
%attr(-,news,news) %{_bindir}/logstat
%attr(-,news,news) %{_bindir}/ngoper
%attr(-,news,news) %{_bindir}/nl-autoupd
%attr(-,news,news) %{_bindir}/nl-del
%attr(-,news,news) %{_bindir}/nl-diff
%attr(-,news,news) %{_bindir}/out-attach
%attr(-,news,news) %{_bindir}/out-freq
%attr(-,news,news) %{_bindir}/out-ls
%attr(-,news,news) %{_bindir}/out-manip
%attr(-,news,news) %{_bindir}/out-rm0
%attr(-,news,news) %{_bindir}/out-rmbsy
%attr(-,news,news) %{_bindir}/outb
%attr(-,news,news) %{_bindir}/outb-kill
%attr(-,news,news) %{_bindir}/pktdebug
%attr(-,news,news) %{_bindir}/pktmore
%attr(-,news,news) %{_bindir}/pkttmpl
%attr(-,news,news) %{_bindir}/recvuu
%attr(-,news,news) %{_bindir}/runchklock
%attr(-,news,news) %{_bindir}/runinc
%attr(-,news,news) %{_bindir}/senduu
%attr(-,news,news) %{_bindir}/senduumail
%attr(-,news,news) %{_bindir}/sumcrc
%attr(-,news,news) %{_libdir}/libfidogate.a
%attr(-,news,news) %{_libdir}/libfidogate.la
%attr(-,news,news) %{_libdir}/libfidogate.so
%attr(-,news,news) %{_libdir}/libfidogate.so.5
%attr(-,news,news) %{_libdir}/libfidogate.so.5.0.0
%attr(-,news,news) %{_libexecdir}/charsetc
%attr(-,news,news) %{_libexecdir}/confval
%attr(-,news,news) %{_libexecdir}/ftn2ftn
%attr(-,news,news) %{_libexecdir}/ftn2rfc
%attr(-,news,news) %{_libexecdir}/ftnafmail
%attr(-,news,news) %{_libexecdir}/ftnafpkt
%attr(-,news,news) %{_libexecdir}/ftnflo
%attr(-,news,news) %{_libexecdir}/ftnin
%attr(-,news,news) %{_libexecdir}/ftninpost
%attr(-,news,news) %{_libexecdir}/ftninrecomb
%attr(-,news,news) %{_libexecdir}/ftnmail
%attr(-,news,news) %{_libexecdir}/ftnpack
%attr(-,news,news) %{_libexecdir}/ftnroute
%attr(-,news,news) %{_libexecdir}/ftntick
%attr(-,news,news) %{_libexecdir}/ftntickpost
%attr(-,news,news) %{_libexecdir}/ftntoss
%attr(-,news,news) %{_libexecdir}/report_traffic
%attr(-,news,news) %{_libexecdir}/rfc2ftn
%attr(-,news,news) %{_libexecdir}/send-fidogate

%dir %attr(700,news,news) %{_sysconfdir}/fidogate
%dir %attr(700,news,news) %{_localstatedir}/log/fidogate
%dir %attr(700,news,news) %{_localstatedir}/lib/fidogate
%dir %attr(700,news,news) %{_localstatedir}/lib/fidogate/seq
%dir %attr(700,news,news) %{_localstatedir}/lock/fidogate
%dir %attr(700,news,news) %{_localstatedir}/spool/fidogate
%dir %attr(770,news,news) %{_localstatedir}/spool/fidogate/bt
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
%config(noreplace) %attr(600,news,news) %{_localstatedir}/lib/fidogate/areas.bbs.sample
%config(noreplace) %attr(600,news,news) %{_localstatedir}/lib/fidogate/fareas.bbs.sample

%changelog
