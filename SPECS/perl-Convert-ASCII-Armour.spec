Name:           perl-Convert-ASCII-Armour
Version:        1.4
Release:        1%{?dist}
Summary:        Convert binary octets into ASCII armoured messages
License:        CHECK(GPL+ or Artistic)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Convert-ASCII-Armour/
Source0:        http://www.cpan.org/authors/id/V/VI/VIPUL/Convert-ASCII-Armour-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Data::Dumper)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module converts hashes of binary octets into ASCII messages suitable
for transfer over 6-bit clean transport channels. The encoded ASCII
resembles PGP's armoured messages, but are in no way compatible with PGP.

%prep
%setup -q -n Convert-ASCII-Armour-%{version}

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
%doc ARTISTIC
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Mar 08 2018 Your Name <wwright@nice.com> 1.4-1
- Specfile autogenerated by cpanspec 1.78.