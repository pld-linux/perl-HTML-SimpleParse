%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	SimpleParse
Summary:	HTML::SimpleParse perl module
Summary(pl):	Modu³ perla HTML::SimpleParse
Name:		perl-HTML-SimpleParse
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f557818d78932654f9ca8dfeae2566b1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::SimpleParse module.

%description -l pl
HTML::SimpleParse jest modu³em pozwalaj±cym analizowaæ pliki HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/SimpleParse.pm
%{_mandir}/man3/*
