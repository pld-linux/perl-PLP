#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%define		pnam	PLP
Summary:	PLP - yet another Perl in HTML embedder
Summary(pl.UTF-8):	PLP - Perl osadzony w dokumentach HTML
Name:		perl-PLP
Version:	3.18
Release:	3
License:	unknown
Vendor:		Jorril Waalboer (Juerd)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JU/JUERD/%{pnam}-%{version}.tar.gz
# Source0-md5:	2d3ad7ecfa0f437fa4e2e0074e9af07e
URL:		http://plp.juerd.nl/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	apache-mod_perl >= 1.26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLP is yet another Perl embedder, primarily for HTML documents. Unlike
with other Perl embedders, there is no need to learn a meta-syntax or
object model: one can just use the normal Perl constructs.

PLP runs under mod_perl for speeds comparable to those of PHP, but can
also be run as a CGI script.

%description -l pl.UTF-8
PLP to kolejne wcielenie osadzonego Perla, głównie dla potrzeb
tworzenia dynamicznych dokumentów HTML. Nie wymaga nauki nowych
znaczników czy meta-tagów, lub kolejnego obiektu w Perlu. Sposób
osadzania Perla w dokumencie HTML przypomina trochę składnię znaną z
języka PHP.

PLP może działać pod kontrolą Apache/mod_perl lub jako skrypt CGI.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "Check 'man PLP' for details about activate PLP with Apache web server"

%postun
echo "Remember to change /etc/httpd/httpd.conf manually"

%files
%defattr(644,root,root,755)
%doc Changes README plp.vim
%dir %{perl_vendorlib}/PLP
%{perl_vendorlib}/PLP/*.pm
%{perl_vendorlib}/PLP/Tie
%{perl_vendorlib}/PLP.pm
%{_mandir}/man[13]/*
