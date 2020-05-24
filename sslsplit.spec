Summary:	Transparent and scalable SSL/TLS interception
Summary(pl.UTF-8):	Przezroczyste i skalowalne przechwytywanie SSL/TLS
Name:		sslsplit
Version:	0.5.5
Release:	1
License:	BSD
Group:		Applications/System
# see also https://github.com/droe/sslsplit/releases
#Source0:	https://github.com/droe/sslsplit/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	https://mirror.roe.ch/rel/sslsplit/%{name}-%{version}.tar.bz2
# Source0-md5:	c9628996a930bd18ce8e635dbedf0362
URL:		https://www.roe.ch/SSLsplit
BuildRequires:	check-devel
BuildRequires:	libevent-devel >= 2
BuildRequires:	libnet-devel >= 1:1.1
BuildRequires:	libpcap-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
Requires:	iproute2
Requires:	iptables
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SSLsplit is a tool for man-in-the-middle attacks against SSL/TLS
encrypted network connections. Connections are transparently
intercepted through a network address translation engine and
redirected to SSLsplit. SSLsplit terminates SSL/TLS and initiates a
new SSL/TLS connection to the original destination address, while
logging all data transmitted. SSLsplit is intended to be useful for
network forensics and penetration testing.

It uses Linux netfilter REDIRECT and TPROXY.

%description -l pl.UTF-8
SSLsplit to narzędzie do ataków MITM przeciw połączeniom sieciowym
szyfrowanym SSL/TLS. Połączenia są w sposób przezroczysty
przechwytywane przez silnik tłumaczenia adresów sieciowych i
przekierowywane do narzędzia SSLsplit. SSLsplit przerywa SSL/TLS i
rozpoczyna nowe połączenie SSL/TLS do oryginalnego adresu docelowego,
logując całe przesyłane dane. SSLsplit jest przeznaczony do śledzenia
sieci oraz testów penetracyjnych.

Narzędzie wykorzystuje funkcjonalność REDIRECT i TPROXY z linuksowego
netfiltra.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	DEBUG_CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	PKG_LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	SYSCONFDIR=%{_sysconfdir}

%{__mv} $RPM_BUILD_ROOT%{_sysconfdir}/sslsplit/sslsplit.conf{.sample,}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.md NEWS.md LICENSE LICENSE.third README.md SECURITY.md
%attr(755,root,root) %{_bindir}/sslsplit
%dir %{_sysconfdir}/sslsplit
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/sslsplit/sslsplit.conf
%{_mandir}/man1/sslsplit.1*
%{_mandir}/man5/sslsplit.conf.5*
