%{!?perl_vendorlib: %define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)}

Name:           perl-XML-Twig
Version:        3.52
Release:        1%{?dist}
Summary:        Perl module for processing huge XML documents in tree mode
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/XML-Twig/
Source0:        http://www.planet-elektronik.de/CPAN//authors/id/M/MI/MIROD/XML-Twig-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(XML::Parser) >= 2.23
Requires:       perl(XML::Parser) >= 2.23

%description
This module provides a way to process XML documents. It is build on top of
XML::Parser.

%prep
%setup -q -n XML-Twig-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check || :
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes check_optional_modules filter_for_5.005 META.json README speedup Twig_pm.slow
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 07 2018 Your Name <wwright@nice.com> 3.52-1
- Specfile autogenerated by cpanspec 1.78.
