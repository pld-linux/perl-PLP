%include	/usr/lib/rpm/macros.perl
%define		pnam	PLP
Summary:	PLP is yet another Perl in HTML embedder
Summary(pl):	Perl osadzony w dokumentach HTML
Name:		perl-PLP
Version:	3.16
Release:	2
License:	GPL
Vendor:		Jorril Waalboer (Juerd)
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-authors/id/J/JU/JUERD/%{pnam}-%{version}.tar.gz
URL:		http://plp.juerd.nl/
Patch0:		%{name}.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	apache-mod_perl >= 1.26
Requires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLP is yet another Perl embedder, primarily for HTML documents. Unlike
with other Perl embedders, there is no need to learn a meta-syntax or
object model: one can just use the normal Perl constructs.

PLP runs under mod_perl for speeds comparable to those of PHP, but can
also be run as a CGI script.

%description -l pl
PLP to kolejne wcielenie osadzonego perla, g³ównie dla potrzeb
tworzenia dynamicznych dokumentów HTML. Nie wymaga nauki nowych
znaczników czy meta-tag'ów, lub kolejnego obiektu w perlu. Sposób
osadzania perla w dokumencie HTML przypomina trochê skladniê znan± z
jêzyka PHP.

PLP moze dzialac pod kontrola Apache/mod_perl lub jako skrypt CGI.

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README plp.vim
%dir %{perl_sitelib}/PLP
%{perl_sitelib}/PLP/*.pm
%{perl_sitelib}/PLP/Tie
%{perl_sitelib}/PLP.pm
%{_mandir}/man[13]/*
