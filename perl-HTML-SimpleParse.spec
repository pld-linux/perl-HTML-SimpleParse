#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	SimpleParse
Summary:	HTML::SimpleParse - a bare-bones HTML parser
Summary(pl):	HTML::SimpleParse - analizator sk³adniowy "go³ego szkieletu" HTML-a
Name:		perl-HTML-SimpleParse
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f557818d78932654f9ca8dfeae2566b1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTML::SimpleParse module is a simple HTML parser.  It is similar
in concept to HTML::Parser, but it differs from HTML::TreeBuilder in a
couple of important ways.

%description -l pl
HTML::SimpleParse jest prostym modu³em pozwalaj±cym analizowaæ pliki
HTML. Jest podobny w idei do HTML::Parser, ale ró¿ni siê w kilku
istotnych sprawach od HTML::TreeBuilder.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/SimpleParse.pm
%{_mandir}/man3/*
