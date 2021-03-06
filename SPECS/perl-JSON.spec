Name:           perl-JSON
Version:        2.61
Release:        1%{?dist}
Summary:        JSON (JavaScript Object Notation) encoder/decoder
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/JSON/
Source0:        http://www.cpan.org/authors/id/M/MA/MAKAMAKA/JSON-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON::XS) >= 2.34
BuildRequires:  perl(Test::More)
Requires:       perl(JSON::XS) >= 2.34
Requires:       perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
************************** CAUTION ********************************
* This is 'JSON module version 2' and there are many differences  *
* to version 1.xx                                                 *
* Please check your applications using old version.              *
*   See to 'INCOMPATIBLE CHANGES TO OLD VERSION'                  *
*******************************************************************

%prep
%setup -q -n JSON-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Mar 07 2018 Your Name <wwright@nice.com> 2.61-1
- Specfile autogenerated by cpanspec 1.78.
