%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	SimpleParse
Summary:	HTML::SimpleParse perl module
Summary(pl):	Modu� perla HTML::SimpleParse
Name:		perl-HTML-SimpleParse
Version:	0.11
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::SimpleParse module.

%description -l pl
HTML::SimpleParse jest modu�em pozwalaj�cym analizowa� pliki HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/HTML/SimpleParse.pm
%{_mandir}/man3/*
