Summary:	Transparent and scalable SSL/TLS interception
Name:		sslsplit
Version:	0.4.11
Release:	3
License:	BSD
Source0:	https://github.com/droe/sslsplit/archive/%{version}.tar.gz
# Source0-md5:	37fe63d0b60268ae48e797a22a39c2da
Group:		Applications/System
URL:		http://www.roe.ch/SSLsplit
BuildRequires:	check-devel
BuildRequires:	libevent-devel
BuildRequires:	openssl-devel
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

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	DEBUG_CFLAGS="%{rpmcflags} %{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -p %{name} $RPM_BUILD_ROOT%{_bindir}
cp -p %{name}.1  $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md NEWS.md
%attr(755,root,root) %{_bindir}/sslsplit
%{_mandir}/man1/sslsplit.1*
